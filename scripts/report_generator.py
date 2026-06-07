import boto3
import json

logs = boto3.client('logs')
s3 = boto3.client('s3')

LOG_GROUP = "/ecs/log-analytics"
BUCKET = "log-analytics-reports-bucket-344211401727"

events = logs.filter_log_events(
    logGroupName=LOG_GROUP
)

total = len(events["events"])

errors = 0

for event in events["events"]:

    if "ERROR" in event["message"]:
        errors += 1

report = {
    "total_events": total,
    "error_events": errors
}

s3.put_object(
    Bucket=BUCKET,
    Key="daily-report.json",
    Body=json.dumps(report)
)

print(report)