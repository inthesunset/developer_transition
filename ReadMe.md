# Investigate developers transition among 4 JS web-end frameworks (angular, ember, react, vue) based on importing framework related packages

### STEPS and Results
1. **RQ1:** How are the usages of the four frameworks?
   *step 1:*  
   Filtered out developers who used at least one of the 4 frameworks based on c2bPtaPKGPJS.{0..31}.gz  
   *result 1:*  
   Extracted out **2143446** unique author ids for **3149813** unique projects.  

   *Further investigation result 2:*  

   **frameworks and the corresponding author num**  

   |framework|\# author ids|
   |:---:|:---:|
   |react|1195016|
   |angular|848227|
   |ember|149618|
   |vue|379739|

   **num of frameworks used per developer**  

   | \# frameworks used | \# author ids |
   |:---:|:---:|
   |1|1779290|
   |2|305578|
   |3|52366|
   |4|6264|

   **Possible combinations of frameworks**  

   |react|angular|ember|vue|\# author ids|
   |:---:|:---:|:---:|:---:|:---:|
   |1|0|0|0|938301|
   |0|1|0|0|568515|
   |0|0|0|1|256951|
   |1|1|0|0|118480|
   |0|1|1|0|86115|
   |1|0|0|1|77579|
   |1|1|1|0|30836|
   |0|1|0|1|17085|
   |1|1|0|1|16969|
   |0|0|1|0|15523|
   |1|1|1|1|6264|
   |1|0|1|0|5989|
   |0|1|1|1|3963|
   |1|0|1|1|598|
   |0|0|1|1|330|

   **single framework usage ratio among all its cases**

   |framework|percentage(%)|
   |:---:|:---:|
   |react|78.5|
   |angular|67.0|
   |ember|10.4|
   |vue|67.7|

   *conclusions:*  
   Developers are more likely to use single framework than using multiple ones, except for ember users.

2. **RQ2:** Did we see migration happen? If yes, give one example.
   *step 2:*  
   We are more interested in authors that used multiple frameworks, where migration might appear.
   I selected author ids that used *react* and *angular* exclusively, given that we have more use cases and react is comparatively new so we would be more likely to find migrations.
   1. filter out data for react + angular
   2. cluster based on author id, check the timeline of commits(that make changes to file where such pkg was imported), plot density of commits within study period, if one drop while the other increase, indicating a migration might happened. (rough version, )


<!---
2. *step 2:*  
   RQ1: Does developer transfer from one framework to another?
   1. create author 2 pkgs by time
   2. select author that has clear transfer trace, i.e., without using multiple frameworks at same time  
   *result 2:* This is a subset of case 2 in step 3. Please refer to step 3 result for more details.   One example:
   - Developer author id: emmett <eragnew@gmail.com>
   - Prj1: eragnew_moment-app framework1: angular Time: Oct 23, 2015
   - Prj2: eragnew_chirper-react-flux-demo-app framework2: react Time: Nov 30, 2015
3. *step 3:*  
   RQ2: What are the trends of migration? (detection)  
   Assumption/Expectation: (case 3, 4, 5 need more detailed analysis of time period)
    - **case 1:** developer may only use single framework
    - **case 2:** developer transfer has clear separate use cases and ends up with one framework
    - **case 3:** developer transfer use multiple frameworks during one period and ends up with one framework
    - **case 4:** developer transfer use multiple frameworks during one period and continue with them
    - **case 5:** developer transfer went back to original framework after trials  
  *preliminary results:*  
    - **case 1:** this is the majority: 383890 out of 411268 uses only one framework
    - **case 2:** this is the second majority: 15632 out of 411268
    - **case 3-5:** **TODO** (require more careful analysis on  time period) => 5993
    - **multiple frameworks involved in single blob:** => 5753
4. *step 4:*  
   RQ3: Maybe like what are reasons? (qualitative study?)
--->
