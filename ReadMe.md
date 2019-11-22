#Investigate developers transition among 4 JS web-end frameworks (angular, ember, react, vue) based on importing framework related packages

### STEPS and Results
1. *step 1.* Filtered out developers who used at least one of the 4 frameworks based on b2cPtaPKGJJS  
   *result 1.* Extracted out **411257** unique author ids for total **2607851** use cases(blobs), and **491844** unique projects.  
   *Further investigation result 2.* StandAlone case( use only one framework) **v.s.** Multi: Among all use cases, (Framework:#) => angular:  811339, ember: 30095, react: 1629007, vue: 160679  
   StandAlone: angular: 794668, ember: 24276, react: 1612833, vue: 154004
   *conclusion* The majority only use one framework.
2. *step 2.* RQ1: Does developer transfer from one framework to another?
   1. create author 2 pkgs by time
   2. select author that has clear transfer trace, i.e., without using multiple frameworks at same time

3. *step 3.* RQ2: What are the trends of migration? (detection)
   Assumption/Expectation: (case 3, 4, 5 need more detailed analysis of time period)
    - **case 1:** developer may only use single framework
    - **case 2:** developer transfer has clear separate use cases and ends up with one framework
    - **case 3:** developer transfer use multiple frameworks during one period and ends up with one framework
    - **case 4:** developer transfer use multiple frameworks during one period and continue with them
    - **case 5:** developer transfer went back to original framework after trials
4. *step 4.* RQ3: Maybe like what are reasons? (qualitative study?)
