# Introduction
For this activity, I researched some different security tools with AI features that are currently available on the market today. I chose specific tools for this activity because it is rare to see a category of tools all have the same AI features. To find these tools, I used the following lists as a starting point to explore further:
- https://cycode.com/blog/ai-cybersecurity-tools/
- https://strapi.io/blog/best-ai-security-tools

## [IBM Tools](https://www.ibm.com/solutions/ai-cybersecurity)
IBM has several tools available which utilise some sort of AI enhancements. These tools are IBM Verify, IBM Guardium, IBM Trusteer, and IBM MaaS360.

IBM Verify is a cloud-based identity and access management platform. It is primarily used in organisations, and connects their existing identity management tools into a sort of "hybrid" identity access system. It uses machine learning to identify potential threats in real-time.

IBM Guardium is a data security platform designed to protect sensitive data throughout its lifecycle across a range of environments with real-time monitoring, auditing, and protection. It allows activity (including who has accessed data and for what purpose) to be monitored, performs vulnerability assessments to identify weaknesss, provides encryption mechanisms to protect data from unauthorised access, ensures compliance with data protection laws, and more. It uses machine learning to provide quicker identification of potential threats (including abnormal behaviour) in real time, and sends alerts whenever data is at risk through its Guardium Data Detection and Response (DDR) tool.

IBM Trusteer is a family of cloud-based services which uses machine learning to assess risk, detect fraud, and authenticate users. The services available under Trusteer include Trusteer Pinpoint Detect (which allows organisations to quickly establish digital identity trust), Trusteer Pinpoint Assure (which detects and predicts the risk of fraudulent intent in real-time), and Trusteer Rapport (which detects and prevents malware and phishing attacks). This detection is done using a multilayered risk assessment, using data from the user's device (like if it has malware or is being emulated), connected network (like the location and whether a VPN is in use), biometrics (comparing behavioural data like keystrokes, mouse movement, session length, etc with previous sessions), account data (like transactional data), and other threat intelligence (like data from the dark web and emerging threats).

## [Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot)
Microsoft Security Copilot is a security assistant/tool which leverages large language model (LLM) technology to help increase the capability of defenders and improve security outcomes. It integrates into Microsoft products like Microsoft Sentinel (a cloud-based security information and event management solution), Microsoft Defender (an antivirus), Microsoft Intune (a cloud-based endpoint management solution), Microsoft Entra (a cloud-based identity and access management solution), and Microsoft Purview (a data security and management tool). Although these all utilise AI in various ways (such as Purview using machine learning to identify sensitive data risks), Security Copilot is a completely separate tool in addition to these. Security Copilot gains context for security issues through Microsoft's own security solutions as well as third-party plugins (which gives it access to logs, alerts, incidents, policies, threat intelligence, and organisation data). This information is then used to allow security teams to prompt it, triggering it to process the prompt (using custom-tuned models based on OpenAI's offerings) with the context it knows which produces a response to handle the security team's request efficiently and completely.

Microsoft suggests that there are several primary use cases for Security Copilot. The first use case they suggest is investigating security threats, with Security Copilot giving security teams context for security incidents so that they can quickly triage and remediate the incident with step-by-step guidance. They also suggest it can be used to troubleshoot IT issues faster, with Security Copilot synthesising any relevant information so that the issue can be resolved quickly. The final major suggestion is that it can be used to define new security policies which are cross-referenced with already existing security policies allowing organisations to implement new policies faster. There are other use cases which they suggest, but they are similar to these three.

## [GitHub Advanced Security](https://github.com/security/advanced-security)
GitHub has some additional security features available to developers to enhance code security, collectively known as GitHub Advanced Security. The products part of GitHub Advanced Security are GitHub Code Security and GitHub Secret Protection.

GitHub Code Security is a set of features which help increase the security of code published on GitHub. It includes code scanning (searching for potential security vulnerabilities and coding errors using CodeQL), Copilot Autofix (which automatically generates fixes for code scanning alerts), security campaigns, custom auto-triage rules for Dependabot (managing Dependabot alerts by automating how alerts are processed), dependency review (seeing details of vulnerable versions of dependencies before pull requests are merged), and security overview. Some of these features leverage large language models (LLMs) to find and fix vulnerable code in real time, reducing the risks associated with these issues. The initial scanning of repositories is done using static analysis tools like CodeQL (with the option of using a third-party scanning tool), which displays the results as code scanning alerts. Copilot Autofix, which uses an LLM model, can then be used to implement the suggested changes.

GitHub Secret Protection is a set of features which, as the name implies, protects secrets in GitHub repositories. It includes secret scanning (which detects secrets that have been pushed into a repository), push protection (which prevents secrets from being leaked by blocking commits containing secrets), Copilot secret scanning (which uses LLMs to detect unstructured credentials which have been pushed into a repository), custom patterns (which detects and prevents leaks of organisation-specific secrets), delegations (which is an approval process for better control over who in an organisation can perform sensitive actions), security campaigns (remediating exposed secrets), and security overview.

## [Amazon Macie](https://aws.amazon.com/macie/) and [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
Amazon Macie is a security tool from Amazon designed to discover sensitive data using machine learning/pattern matching/natural language processing, and provide visibility into and protection against data security risks. It evaluates your Amazon S3 buckets (an object storage service) and generates findings to notify you of security issues like misconfigured buckets, unencrypted buckets, publicly accessible buckets, and buckets shared outside your organisation which may introduce risks like unauthorised access or data leakage. It also analyses objects in S3 buckets, recognising sensitive data like personally identifiable information that may exist in the buckets. This has the additional side effect of helping data protection regulations be met. Macie runs continually on all S3 buckets, automatically creating alerts on the AWS dashboard when it finds anything that could be a security issue.

Amazon GuardDuty, another security tool from Amazon, is a threat detection service which continually monitors your AWS accounts, containers, workloads, and data for malicious activity using machine learning which integrates into the current AWS workflow. It scans EC2/ECS instances, Lambda functions, EKS clusters, S3 buckets, and Aurora instances for any suspicious activity like communication with known threat actor servers, requests coming from unusual locations, API call patterns commonly used to discover misconfigured permissions, suspicious logins, etc. If any potential threats are found, it generates detail findings about the issue in the GuardDuty console. Additionally, it has a malware protection feature which can be used to detect malicious files on EBS volumes or AWS backups to verify that they are clean.

## [Darktrace ActiveAI Security Platform](https://www.darktrace.com/platform)
Darktrace ActiveAI Security Platform is a cybersecurity tool from Darktrace which uses unsupervised machine learning to detect any anomalous behaviour in real-time to prevent threats. It does this by using behavioural analysis and learning on your organisations' data (rather than being trained on what an attack "should" look like using lots of historical data) to provide the most accurate threat detection possible. By doing this, it can understand normal behaviour for organisations (including employee behaviour, systems, and data) and identify suspicious behaviour. As it employs machine learning, it constantly evolves its understanding of what "normal" for an organisation looks like. It is a comprehensive tool, providing defence for email, identity management systems, cloud-based systems, network systems, and endpoint systems, with integrations with existing security infrastructure to create a unified solution.

It is unlike many other threat detection systems for a few reasons. Unlike traditional security solutions, it does not require manual intervention and instead purely learns from existing patterns to detect and autonomously respond to potential threats. Darktrace also use an approach to security that is proactive (i.e. it aims to identify weaknesses before they are exploited), unlike traditional solutions which are reactive (i.e. they focus on responding to incidents after they've occurred). 

<br>

# References
Cycode Ltd. "The 10 Best AI Cybersecurity Tools in 2026". Accessed: Mar. 30, 2026. [Online]. Available: https://cycode.com/blog/ai-cybersecurity-tools/

P. Bratslavsky. "Best AI Security Tools for 2026 (Top 10 Compared)". Strapi. Accessed: Mar. 30, 2026. [Online]. Available: https://strapi.io/blog/best-ai-security-tools

IBM. "Artificial intelligence (AI) cybersecurity solutions". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/solutions/ai-cybersecurity

IBM. "IBM Verify". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/verify

IBM. "Overview and use cases". Accessed: Mar. 30, 2026. [Online]. Available: https://docs.verify.ibm.com/verify/docs/use-cases

IBM. "Protect your data across its lifecycle with IBM Guardium". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/guardium

IBM. "Guardium Data Protection". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/guardium-data-protection

IBM. "Guardium Data Security Center". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/guardium-data-security-center

A. K. "What is IBM Guardium and use cases of IBM Guardium?". DevOpsSchool. Accessed: Mar. 30, 2026. [Online]. Available: https://www.devopsschool.com/blog/what-is-ibm-guardium-and-use-cases-of-ibm-guardium/

IBM. "Guardium DDR (Data Detection and Response)". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/guardium-data-detection-response

IBM. "IBM Trusteer Solutions". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/trusteer

IBM. "IBM Trusteer Rapport". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/trusteer-rapport

IBM. "IBM Trusteer Pinpoint Detect". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/trusteer-pinpoint-detect

IBM. "IBM Trusteer Pinpoint Assure". Accessed: Mar. 30, 2026. [Online]. Available: https://www.ibm.com/products/trusteer-pinpoint-assure

Microsoft. "What is AI for cybersecurity?". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-au/security/business/security-101/what-is-ai-for-cybersecurity

Microsoft. "What is Microsoft Security Copilot?". Accessed: Mar. 30, 2026. [Online]. Available: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot

Microsoft. "MICROSOFT SECURITY COPILOT". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-au/security/business/ai-machine-learning/microsoft-security-copilot

Microsoft. "What is Microsoft Sentinel security information and event management (SIEM)?". Accessed: Mar. 30, 2026. [Online]. Available: https://learn.microsoft.com/en-us/azure/sentinel/overview?tabs=defender-portal

Microsoft. "Microsoft Intune". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-us/security/business/microsoft-intune

Microsoft. "Microsoft Entra". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-au/security/business/microsoft-entra

Microsoft. "Microsoft Purview". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-au/security/business/microsoft-purview

GitHub, Inc. "GITHUB ADVANCED SECURITY". Accessed: Mar. 30, 2026. [Online]. Available: https://github.com/security/advanced-security

GitHub, Inc. "About GitHub Advanced Security". Accessed: Mar. 30, 2026. [Online]. Available: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security

GitHub, Inc. "GitHub Advanced Security (GHAS)". Accessed: Mar. 30, 2026. [Online]. Available: https://learn.github.com/learning-pathways/github-advanced-security

Microsoft. "GitHub Advanced Security (GHAS)". Accessed: Mar. 30, 2026. [Online]. Available: https://www.microsoft.com/en-us/securityengineering/sdl/ghas

GitHub, Inc. "About code scanning". Accessed: Mar. 30, 2026. [Online]. Available: https://docs.github.com/en/code-security/concepts/code-scanning/about-code-scanning

Amazon Web Services, Inc. "AI/ML for security". Accessed: Mar. 30, 2026. [Online]. Available: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/ai-ml.html

Amazon Web Services, Inc. "Amazon Macie". Accessed: Mar. 30, 2026. [Online]. Available: https://aws.amazon.com/macie/

Amazon Web Services, Inc. "Amazon Macie Best Practices". Accessed: Mar. 30, 2026. [Online]. Available: https://aws.github.io/aws-security-services-best-practices/guides/macie/

A. Novotny. "What is Amazon Macie & How does it Protect Your Sensitive Data?". stormit.cloud. Accessed: Mar. 30, 2026. [Online]. Available: https://www.stormit.cloud/blog/what-is-amazon-macie/

Amazon Web Services, Inc. "Amazon GuardDuty". Accessed: Mar. 30, 2026. [Online]. Available: https://aws.amazon.com/guardduty/

Amazon Web Services, Inc. "Monitoring threats with Amazon GuardDuty RDS Protectionfor Amazon Aurora". Accessed: Mar. 30, 2026. [Online]. Available: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/guard-duty-rds-protection.html

Amazon Web Services, Inc. "Amazon GuardDuty Best Practices". Accessed: Mar. 30, 2026. [Online]. Available: https://aws.github.io/aws-security-services-best-practices/guides/guardduty/

Darktrace Holdings Limited. "ActiveAI Security Platform". Accessed: Mar. 31, 2026. [Online]. Available: https://www.darktrace.com/platform

Darktrace Holdings Limited. "The most comprehensive AI security platform". Accessed: Mar. 31, 2026. [Online]. Available: https://www.darktrace.com/products

Darktrace Holdings Limited. "Darktrace / SECURE AI". Accessed: Mar. 31, 2026. [Online]. Available: https://www.darktrace.com/products/secure-ai

Darktrace Holdings Limited. "Cyber AI: Augment your security team and stop novel threats". Accessed: Mar. 31, 2026. [Online]. Available: https://www.darktrace.com/cyber-ai

L. Wallart. "Darktrace, The Future of Cyber Security". Devoteam. Accessed: Mar. 31, 2026. [Online]. Available: https://www.devoteam.com/expert-view/darktrace-future-of-cyber-security/