# k-Anonymity
To preserve privacy in offline situations (like datasets), k-anonymity is often used. This is a data anonymisation technique used to protect individuals' privacy. It is often used on datasets which have to be released while not disclosing individuals' personal information. A dataset is considered k-anonymous when the quasi-identifiers (information that can be used to identify individuals when combined) for each individual is indistinguishable from at least *K* - 1 others (i.e. the data is not unique to individuals and therefore cannot be used to identify them, preserving their privacy). For example, if *K* = 5, then there are at least 5 sets of every data combination in the dataset.

This is done in various ways, like generalisation and suppression of data. Generalisation involves broadening data from specific information to more general information. This can be applied to fields like locations (generalising suburbs to city/state/country depending on the data) or ages (generalising into age brackets). Suppression, on the other hand, is completely removing an attribute from the dataset entirely. This is generally used for data that is not important or relevant to the purpose of the data collection (which often includes names of individuals in most cases).

This technique helps prevent malicious actors from performing attacks like re-identification attacks. These attacks occur when certain knowledge of individuals (such as a certain combination of quasi-identifiers) is used to re-identify individuals in a dataset. This could, potentially, expose information about them to the attacker if the dataset includes more private information. Higher *K* values result in less risk of re-identification, but this comes at the caveat that it decreases the utility of the data. There is, therefore, a trade-off between privacy and utility when using k-anonymity.

k-anonymity is still vulnerable to a few different attacks, like homogeneity attacks or background knowledge attacks. Homogeneity attacks occur when every member with a given combination of identifiers have the same (or with little variance) sensitive values. This means that an attacker can still infer private information about individuals with certainty. Background knowledge attacks occur when extra background knowledge is known about an individual, allowing an attacker to still re-identify them despite the k-anonymity of the data.

The provided evidence is based on the example found at https://github.com/OpenMined/PyDP/tree/dev/examples/Tutorial_1-carrots_demo, but instead of using differential privacy I used k-anonymity.

<br>

# References
G. Trotino. "What is K Anonymity and Why Data Pros Care". K2VIEW. Accessed: Mar. 19, 2026. [Online]. Available: https://www.k2view.com/blog/what-is-k-anonymity

H. Devane. "Everything You Need to Know About K-Anonymity". Immuta Inc. Accessed: Mar. 19, 2026. [Online]. Available: https://www.immuta.com/blog/k-anonymity-everything-you-need-to-know-2021-guide/

Google. "Computing k-anonymity for a dataset". Accessed: Mar. 19, 2026. [Online]. Available: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity

NS Academy. "Explain k-anonymity and its limitations". Accessed: Mar. 19, 2026. [Online]. Available: https://medium.com/@sharetonschool/explain-k-anonymity-and-its-limitations-230c0f0d32b4