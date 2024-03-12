import boto3
from openpyxl import Workbook

def get_listener_rules(lb_arn):
    elbv2_client = boto3.client('elbv2')
    response = elbv2_client.describe_listeners(LoadBalancerArn=lb_arn)

    listener_rules = {}
    for listener in response['Listeners']:
        listener_arn = listener['ListenerArn']
        listener_port = listener['Port']
        listener_protocol = listener['Protocol']

        rules_response = elbv2_client.describe_rules(ListenerArn=listener_arn)
        rules = rules_response.get('Rules', [])

        listener_rules[listener_port] = {
            'Protocol': listener_protocol,
            'Conditions': []
        }

        rule_arns = [rule['RuleArn'] for rule in rules]
        for rule_arn in rule_arns:
            rule_response = elbv2_client.describe_rules(RuleArns=[rule_arn])
            conditions = rule_response['Rules'][0].get('Conditions', [])

            listener_rules[listener_port]['Conditions'].extend(conditions)

    return listener_rules

def get_lb_scheme(lb_arn):
    elbv2_client = boto3.client('elbv2')
    response = elbv2_client.describe_load_balancers(LoadBalancerArns=[lb_arn])
    lb_scheme = response['LoadBalancers'][0]['Scheme']
    return lb_scheme

def main():
    elbv2_client = boto3.client('elbv2')
    response = elbv2_client.describe_load_balancers()

    wb = Workbook()
    ws = wb.active
    ws.append(["LOAD BALANCER", "LISTENER", "CONDITIONS", "LB DNS", "EXTERNAL-INTERNAL"])

    for lb in response['LoadBalancers']:
        lb_name = lb['LoadBalancerName']
        lb_arn = lb['LoadBalancerArn']
        lb_dns = lb['DNSName']
        lb_scheme = get_lb_scheme(lb_arn)

        listener_rules = get_listener_rules(lb_arn)
        for listener_port, rules_info in listener_rules.items():
            listener_info = f"Listener Port: {listener_port}, Protocol: {rules_info['Protocol']}"
            conditions_list = []
            for condition in rules_info['Conditions']:
                field = condition.get('Field', 'Unknown')
                values = condition.get('Values', 'Unknown')
                condition_str = f"Field: {field}, Value: {values}"
                conditions_list.append(condition_str)
            conditions = "\n".join(conditions_list)
            ws.append([lb_name, listener_info, conditions, lb_dns, lb_scheme])

    wb.save("arco-prod-us-east-1.xlsx")

if __name__ == "__main__":
    main()
