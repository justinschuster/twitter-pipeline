# Language Meter

Uses Twitter to gauge daily programming language interest

Technologies Used:
- Twitter Api
- Python
- AWS lambda
- AWS s3
- AWS Redshift
- *maybe* GCP Data Studio

TODO:
- streaming twitter api response
    - currently limited in number of tweets retrieved

RISK FACTORS
- api rate limit
    - 2 million per month
- differentiating programming languages from other things
    - Python (code) vs python (pet)