import boto3
from datetime import datetime, timedelta

def get_aws_config_client():
    return boto3.client('config')

def get_config_rules():
    config_client = get_aws_config_client()
    response = config_client.describe_config_rules()
    return response['ConfigRules']

def get_compliance_details(config_rule_name):
    config_client = get_aws_config_client()
    response = config_client.get_compliance_details_by_config_rule(
        ConfigRuleName=config_rule_name,
        ComplianceTypes=['NON_COMPLIANT'],
        Limit=100
    )
    return response['EvaluationResults']

def drift_detector(config_rule_name, baseline_config):
    config_rules = get_config_rules()

    if config_rule_name not in [rule['ConfigRuleName'] for rule in config_rules]:
        print(f"Config rule '{config_rule_name}' not found.")
        return

    current_compliance_details = get_compliance_details(config_rule_name)

    drift_detected = False

    for evaluation_result in current_compliance_details:
        resource_id = evaluation_result['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceId']
        compliance_type = evaluation_result['ComplianceType']

        if resource_id in baseline_config and baseline_config[resource_id] != compliance_type:
            print(f"Drift detected for resource '{resource_id}': {compliance_type} (Expected: {baseline_config[resource_id]})")
            drift_detected = True

    if not drift_detected:
        print("No drift detected. Infrastructure is in compliance with the baseline.")

if __name__ == "__main__":
    # Define your baseline configuration here
    baseline_config = {
        'resource_id_1': 'COMPLIANT',
        'resource_id_2': 'COMPLIANT',
        # Add more resources and their expected compliance states
    }

    # Specify the AWS Config rule to monitor
    config_rule_name = 'your_config_rule_name'

    # Run the drift detector
    drift_detector(config_rule_name, baseline_config)
