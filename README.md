# Project2_SecureS3


# AWS S3 Data Protection & Automated Security Response

## Project Overview

This project demonstrates a secure and resilient S3-based storage architecture for protecting sensitive data in AWS. It integrates data encryption, fine-grained access control, audit logging, real-time alerts, and automated recovery to simulate a real-world enterprise-grade security workflow.

## Architecture Diagram

![Architecture Diagram](./architecture-diagram.png)

## Features & Technologies

| Feature                              | Description                                                  |
|--------------------------------------|--------------------------------------------------------------|
|  S3 encryption (SSE-S3)             | Secure all stored data automatically                        |
|  IAM Tag-based access control       | Enforce least privilege via identity tags                   |
|  CloudTrail logging (Data Events)   | Monitor and log S3 object access and deletion                |
|  CloudWatch Metrics + SNS           | Trigger alerts on unusual activity                          |
|  EventBridge + Lambda               | Automatically restore deleted objects from backup bucket     |
|  GuardDuty integration              | Real-time threat detection on AWS account activities         |


## Getting Started

1. Create and configure S3 buckets (main + backup) with SSE enabled  
2. Attach IAM role with tag-based permission policies  
3. Enable CloudTrail with Data Event tracking for the main bucket  
4. Set up Metric Filters and CloudWatch Alarms with SNS notification  
5. Deploy Lambda function triggered by EventBridge for object recovery  
6. Integrate GuardDuty and DynamoDB for advanced threat analytics  

## What I Learned

- How to design a secure S3 architecture using IAM tag policies  
- Event-driven architecture for automated incident response  
- AWS Lambda integration with EventBridge and CloudTrail  
- Monitoring and notification using CloudWatch and SNS  
- Security best practices in data protection and recovery  
- GuardDuty threat detection and response automation  

## Interview Highlights

- Demonstrated understanding of S3 access control, encryption, and auditing  
- Showcased end-to-end automated recovery mechanism for business continuity  
- Applied serverless services to build scalable, real-world solutions  
- Good grasp of how to implement compliance and security monitoring in AWS  
- Experienced with automation pipelines and security response playbooks  

## TL;DR (Summary for Recruiters)

> Designed and implemented an AWS security automation project focused on S3 data protection. Includes IAM tag-based control, audit logging with CloudTrail, alerting with CloudWatch + SNS, and automatic object recovery via Lambda and EventBridge.
