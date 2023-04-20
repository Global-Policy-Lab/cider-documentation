# Recommendations: Output verification

Cider users should implement governance structures that achieve standards for data ethics, making sure humanitarian programs are targeting and delivering aid to those in need without infringing human rights.

Output verifications increase accountability and transparency with recipients and non-recipients, partners, funders, and humanitarian and development communities as a whole. It also creates the necessary governance to minimize bias and discrimination (which is also present in in-person targeting) and maximize fairness on the large-scale use of sensitive data, exponentiating the positive impact of AI. The verification process should combine internal and external audits, such as a research institution or contracted technical auditor. Other resources for setting up output verifications can be found here:

- [AI for humanitarian action: Human rights and ethics](https://international-review.icrc.org/articles/ai-humanitarian-action-human-rights-ethics-913) from the ICRC (International Committee of the Red Cross)]
- [Understanding artificial intelligence ethics and safety: A guide for the responsible design and implementation of AI systems in the public sector](https://www.turing.ac.uk/sites/default/files/2019-06/understanding_artificial_intelligence_ethics_and_safety.pdf) from the Alan Turing Institute

## Internal audits

- **Targeting comparisons:** It is critical to compare phone-based targeting to alternative targeting mechanisms in the context of interest to ensure that phone-based targeting is the most appropriate method for the circumstances (see the targeting module). Ideally, CDR-based targeting should be compared to any other method that could be feasibly implemented at scale, and the best targeting method should be selected for the program. However, which counterfactual targeting approaches can be assessed depends on which survey data is collected. Geographic targeting methods are valuable counterfactual targeting methods. Typically, some location data will be available (whether self-reported in the survey, recorded by field enumerators with geographic coordinates, or available in administrative data). If this data is available, compare the CDR-based targeting method to geographic targeting at every feasible geography, at minimum at the admin-2 level but ideally at the admin-3 or admin-4 level. If the ground-truth poverty measure in the survey is consumption or income, collect data to construct a proxy-means test and asset index and compare targeting on these proxy poverty measures. Always also compare to random targeting as a naive baseline. 

- **Bias audits:** It is also vital to audit the algorithm for systematic bias for or against specific subgroups. If possible, qualitative or legal work should be conducted to assess which subgroups are vulnerable and should be audited for fairness checks. Qualitative work should consist of interviews or focus groups with program stakeholders, including local government, NGOs, and, most importantly, potential program beneficiaries. Alternatively, fairness classes could be based on the legal context in question, checking fairness for subgroups protected by the law. For example, in the US, race, religion, nationality, sex, age, disability status, and veteran status are all protected classes. The bias audit feature in Cider will present audits for two types of systematic biases: a systematic over- or under-prediction of a subgroup’s poverty, or a systematic over- or under-targeting of a subgroup (known as demographic parity). 

## External audits

External audits provide the transparency needed to stakeholders by allowing third-party verification of an implementer’s results. Auditors often assess if outputs are fair and impartial and if data protection protocols are in place. In addition to transparency, the third-party audits address concerns about the conflict of interest that might exist in internal audits. AI tools applied to the development and humanitarian sectors should aim to achieve the highest accountability standards, and for that, outputs should be independently audited. Cider's open source license and internal audit mechanisms aim to provide sufficient information to be auditable by independent parties. It is encouraged that these independent audits be done by organizations with both the technical capacity and experience in the field.   

More resources on third party audits can be found here: 

- [AI for humanitarian action: Human rights and ethics](https://international-review.icrc.org/articles/ai-humanitarian-action-human-rights-ethics-913) from the ICRC (International Committee of the Red Cross)
- [Brundage et. al. (2020). Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims](https://arxiv.org/pdf/2004.07213.pdf)

Although the Cider team does not endorse any specific auditing company, here is a brief list of organizations focused on AI fairness auditing:

- [Orcaa | O'Neil Risk Consulting & Algorithmic Auditing](https://orcaarisk.com/)
- [Parity AI](https://www.getparity.ai/)
- [Saidot AI](https://www.saidot.ai/)
- [Cognitive Scale](https://www.cognitivescale.com/)
- [Accenture Applied Intelligence](https://www.accenture.com/us-en/services/ai-artificial-intelligence-index)
- [Deloitte | Model Guardian](https://www2.deloitte.com/de/de/pages/risk/solutions/ai-fairness-with-model-guardian.html)
