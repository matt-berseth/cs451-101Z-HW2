# cs451-101Z-HW2
Repository for cs451 HW2 - Unsupervised Learning

## Windows 10/11 Set Up Steps
```powershell
# run the following in a powershell window

# clone the repo
git clone https://github.com/matt-berseth/cs451-101Z-HW2

# path into the repo
cd cs451-101Z-HW2

# create the virtual env
python3.10 -m venv .venv

# activate
.\.venv\Scripts\activate.ps1

# install the deps
python -m pip install --upgrade pip
pip install -r requirements.txt

# launch vscode
code .
```

## Ubuntu 22.04 Set Up Steps
```bash
# run the following in a ubuntu window

# clone the repo
git clone https://github.com/matt-berseth/cs451-101Z-HW2

# path into the repo
cd cs451-101Z-HW2

# create the virtual env
python3 -m venv .venv

# activate
source ./.venv/bin/activate

# install the deps
pip install --upgrade pip
pip install -r requirements.txt

# launch vscode
code .
```

## Instructions
**Machine Learning Homework Assignment - Unsupervised Learning**

**Objective:**  
Use the k-means clustering algorithm to cluster the data contained in `X.txt``. Use an elbow plot
to identify the best value for K.

---

**Dataset:**  
`X.txt` is the data that is being used.

---

**Tasks:**

1. Complete the TODOs in `kmeans_elbow.py` python file.
2. Complete the TODOs in the `kmeans.py` python file.
3. Write a 1-2 page report summarizing the findings of tasks 1 and 2. Include a visual of the elbow plot along with a visual of the final clusters and cluster centroids. Include in the report why you chose a specific value of 'K'. Report needs to include the elbow plot and a final plot with all data points, colored by the cluster they belong to.

---

**Deliverables**:

1. Python code (`kmeans_elbow.py` and `kmeans.py`).
2. Report summarizing findings and insights (`.pdf`).

---

**Notes**:
- Plagiarism will result in a zero for the assignment.
