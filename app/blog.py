# This is not a clean implementation but it's kinda in line with the site design
# It'll probably stay this way until I rewrite the whole site at some point
posts = {
    "discovering-prefect": {
        "title": "Discovering Prefect",
        "date": "01/17/25",
        "mod_date": "01/17/25",
        "tags": ["automation", "python", "bioinformatics"],
        "subtitle": "I was considering using cronjobs just to avoid Airflow. Then I found Prefect.",
    },
    "multi-dev-deployment": {
        "title": "CI/CD with Feature Environments",
        "date": "12/04/24",
        "mod_date": "12/04/24",
        "tags": ["devops", "python", "aws"],
        "subtitle": "Avoid dev deployment collisions! Every branch is worth its own environment.",
    },
    "disctracker": {
        "title": "Ultimate DiscTracker",
        "date": "10/08/24",
        "mod_date": "10/08/24",
        "tags": ["python", "web", "flask", "sports analytics"],
        "subtitle": "The beginnings of an environment for Ultimate Frisbee stat tracking, analytics, real-time AI coaching, and more.",
    },
    "firewalls-in-china": {
        "title": "Studying Network Security in China",
        "date": "06/17/24",
        "mod_date": "06/17/24",
        "tags": ["web", "firewalls", "security"],
        "subtitle": "An overview of my independent study on network security while in China.",
    },
    "flask-sessions": {
        "title": "Where to Put Flask Session Data",
        "date": "06/12/24",
        "mod_date": "06/12/24",
        "tags": ["python", "web", "flask", "sessions"],
        "subtitle": "There is a very easy solution for very simple use cases.",
    },
    "qkd": {
        "title": "Quantum Key Distribution",
        "date": "03/20/24",
        "mod_date": "03/20/24",
        "tags": ["quantum computing", "cryptography"],
        "subtitle": "A quick overview of some quantum cryptography basics.",
    },
    "cicd-pipeline": {
        "title": "CI/CD Pipeline with GitHub Actions",
        "date": "11/30/23",
        "mod_date": "11/30/23",
        "tags": ["devops", "github actions", "aws"],
        "subtitle": "Automate serverless flask testing and deployment with GitHub Actions.",
    },
    "comps": {
        "title": "Physical Reservoir Computing for Classification of Temporal Data",
        "date": "11/01/23",
        "mod_date": "11/30/23",
        "tags": ["deep learning", "chaotic systems", "time series"],
        "subtitle": "My undergrad thesis! Read on for more.",
    },
}


post_list = list(posts.keys())
