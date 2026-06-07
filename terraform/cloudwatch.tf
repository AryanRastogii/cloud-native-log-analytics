resource "aws_cloudwatch_log_group" "app_logs" {

  name = "/ecs/log-analytics"

  retention_in_days = 30
}