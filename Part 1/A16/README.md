# Introduction
For this activity, I discovered three local security incidents (focusing on cybersecurity incidents in particular and using Australia as the "local" entity). Each of these were discovered by doing some quick research on recent cyber attacks in Australia, using a [list of recent incidents in Australia](https://www.webberinsurance.com.au/data-breaches-list). Although there was no reason to specifically use recent incidents for the purposes of this activity, each incident was relevant and were done by separate threat actors so it seemed like the most appropriate thing to do. After identifying which incidents to investigate further, I looked at various articles about the attack as well as any statements by the victim as a cross-reference and extracted the important information to act as evidence for my discovery.

## Incident 1 - [The Legal Practice Board of Western Australia (May 2025)](https://www.lpbwa.org.au/cyber-incident)
In late May 2025, the Legal Practice Board of Western Australia (the LPBWA, an independent body supporting lawyers in Western Australia) detected a cyber attack on its systems by an unauthorised third-party. Although it was quickly detected and contained, it still resulted in the downtime of some of their services including their website and invoicing system. Approximately a week later, the attackers uploaded a small amount of the data online (which contained personal details like contact information and bank account details) but that was (apparently) taken down within 24 hours and the impacted individuals notified. The attackers threatened to disclose more data about the LPBWA in June, releasing some more data online a few days later and even more in November but this data apparently was not from the LPBWA. By early December 2025, they claimed that the effects of the attack had essentially gone and that there was a low risk of future disclosure of the data.

Although the exact details of the attack were not disclosed by the LPBWA, it was reported by the media that 300GB of data was exfiltrated and that the attack was performed by the Dire Wolf ransomware. This is a new ransomware group, which has targeted several businesses in various countries (including other Australian businesses) according to ransomware.live. According to the Government of Singapore, their attacks are employed by encrypting victims' data on their systems with threats to publicly release the data unless the ransom is paid. The LPBWA was actually one of the first victims of this ransomware gang, and was one of six organisations initially targeted.

## Incident 2 - [Qantas Cyber Incident (June-October 2025)](https://www.qantas.com/au/en/support/information-for-customers-on-cyber-incident.html)
In early July 2025, Qantas Australia confirmed that they had suffered a data breach. The media release they published at the time of the incident stated that approximately 5.7 million of their customers had their data held in the accessed system, including their name, email addresses, frequent flyer details, home address, date of birth, phone numbers, gender, and meal preferences (with the number of entries holding each attribute varying). They claimed that in late June 2025 that they had detected unusual activity on a third-party platform used by Qantas. In mid October 2025, they confirmed that the data was released onto the Dark Web by the attackers.

I could not find any information from Qantas regarding the attack itself, but there were various details uncovered by the media. The ABC reported that the attack was performed by the cybercrime group Scattered Lapsus$ Hunters, who are a group which have attacked several high-profile companies in the last year with the primary motivation of money. In this same article, it is reported that the data was accessed by using social engineering techniques to trick a Qantas call centre worker into handing over access to the data and that the third-party platform used by Qantas was Salesforce (which Google's Threat Intelligence Group also reported, and although they use a different name for the attackers they were reportedly working together). Another ABC article claims that the group claimed that the attack was done because they didn't agree with some of the policies of the Australian government, and that Qantas was one of 40 businesses attacked by this particular cybercrime group. It is also reported that the data was released in October because the deadline for the ransom had passed and Qantas had not paid it.

## Incident 3 - [Pressure Dynamics (June 2025)](https://www.pressuredynamics.com/)
Note that unlike the previous incidents, I could not find any information directly from the business about this cyber attack. However, this information is seemingly coming from reliable sources so it is likely that the business did not want to publicly announce this as it did not impact the public and could cause reputational damage if they said anything.

In mid June 2025, Pressure Dynamics (an engineering contractor based in Perth, WA) was reported to have suffered a data breach. As reported by CyberDaily, the attack stole over 100GB of data from Pressure Dynamics including information like customer reports, technical drawings, and medical reports of employees. It is alleged that this attack was done by the DragonForce ransomware group, who run a "ransomware-as-a-service" operation where they can be hired in return for a cut of any profits. Unlike the other two incidents, the attack focuses on encrypting the data with threats to publish the data online if the ransom is not paid.

<br>

# References
Webber Insurance Services. "THE COMPLETE LIST OF DATA BREACHES IN AUSTRALIA FOR 2018 - 2026". Accessed: Mar. 3, 2026. [Online]. Available: https://www.webberinsurance.com.au/data-breaches-list

Legal Practice Board of Western Australia. "Cyber incident investigation". Accessed: Mar. 1, 2026. [Online]. Available: https://www.lpbwa.org.au/cyber-incident

D. Hollingworth. "WA Legal Practice Board confirms ransomware attack". MomentumMedia. Accessed: Mar. 1, 2026. [Online]. Available: https://www.lawyersweekly.com.au/biglaw/42201-wa-legal-practice-board-confirms-ransomware-attack

Ransomware.live. "Direwolf". Accessed: Mar. 1, 2026. [Online]. Available: https://www.ransomware.live/group/direwolf

Cyber Security Agency of Singapore. "Ongoing Dire Wolf Ransomware Campaign". Accessed: Mar. 1, 2026. [Online]. Available: https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-082/

Qantas Airways Limited. "Information for customers on cyber incident". Accessed: Mar. 1, 2026. [Online]. Available: https://www.qantas.com/au/en/support/information-for-customers-on-cyber-incident.html

Qantas Airways Limited. "UPDATE ON QANTAS CYBER INCIDENT: WEDNESDAY 9 JULY 2025". Accessed: Mar. 1, 2026. [Online]. Available: https://www.qantasnewsroom.com.au/media-releases/update-on-qantas-cyber-incident-wednesday-9-july-2025

R. Whitson and Y. Li. "Frustration mounts among Qantas customers as personal data released on dark web". Australian Broadcasting Corporation. Accessed: Mar. 1, 2026. [Online]. Available: https://www.abc.net.au/news/2025-10-13/frustration-mounts-among-qantas-customers-over-data-breach/105885312

Google Threat Intelligence Group. "The Cost of a Call: From Voice Phishing to Data Extortion". Accessed: Mar. 1, 2026. [Online]. Available: https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion

S. Bryan. "Government holds firm on not negotiating with hackers in wake of Qantas breach". Australian Broadcasting Corporation. Accessed: Mar. 1, 2026. [Online]. Available: https://www.abc.net.au/news/2025-10-12/government-will-not-negotiate-with-hackers-after-qantas-breach/105882936

D. Hollingworth. "Exclusive: WA-based Pressure Dynamics confirms DragonForce ransomware attack". MomentumMedia. Accessed: Mar. 1, 2026. [Online]. Available: https://www.cyberdaily.au/security/12256-exclusive-wa-based-pressure-dynamics-confirms-dragonforce-ransomware-attack