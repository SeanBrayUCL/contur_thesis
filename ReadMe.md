# Contur Profiles
This repository has been created as part of the completion of a research project for the MSc Scientific Computing at UCL.

The focus of the project was the profiling and optimisation of the Contur toolkit, the code for which can be found here https://gitlab.com/hepcedar/contur.

The repository contains a small amount of code, profiling results and the completed thesis written for the project.

The contents of each file the repository are summarised below.

## thesis
Contains the final thesis as a pdf and in the development folder the tex code used to create the thesis.

## profiling_code
Contains one python script which contains code used to profile a Scipy function, see thesis for further details

## profiles
Each folder in this folder contains results from profiling Contur. These profiles folders contain a .prof file which can be read viewed with Snakeviz and png image showing a dot plot of the profiling results (see chapter 3 of the thesis for further details into viewing these results). The folder starts with a profile of Contur before any optimisation was attempted (starting_point) and then each change made gets own folder with updated profiling results. The changes made accumulate with ascending file number, so the final folder (Change_5_list_concatenation) will contain all the optimisation changes made, so can be taken as the final profile of Contur after all the changes made in this project.

The profile sub-folders are:

1. __starting_point__ : First profile of single yoda and grid run made using version of contur at commit 49a67e found here https://gitlab.com/hepcedar/contur/-/tree/49a67e039cf93c88b39dade3dfb7c5f03e780fb2;

2. __Change_1_err_map__ : Profile after commit 5df35e7 found here https://gitlab.com/hepcedar/contur/-/commit/5df35e7e2e3419fb650e3a2611338a9119865425. Note this change was not discussed in the thesis, becuase later changes to the correaltion run in Contur not related to this research project somewhat nullified its effect;

3. __Change_2_sort_blocks__ : Profile after commit 49acaa4a found here https://gitlab.com/hepcedar/contur/-/commit/49acaa4a340e28aa04ac444e80902a32edd9b630;

4. __Change_3_likelihood_optimisation__ : Profile after commit 2769e1c2a found here https://gitlab.com/hepcedar/contur/-/commit/2769e1c2a020efd2de2919db2413309eef8a8e64 . Note one complication here is that this chnage and change 4 was made with the some commit. Chnage 4 just adds a single if statement, so to produce this profile we ran this version of Contur excluding the additionally if statement. This was to isolate the impact of the change reducing the calls to the survival function (see chapter 5 in thesis for further details).

5. __Change_4 debugger__: Profile after commit 2769e1c2a found here https://gitlab.com/hepcedar/contur/-/commit/2769e1c2a020efd2de2919db2413309eef8a8e64. This is the same commit as the previous change, except when we profile with this commit for change 4 we include the additional if statement (so commentary for previous folder). So this profile is really seeing the impact of adding the single if statement.

6. __Change_5 List_concatenation__: Given by commit c6d26961 in branch further_optimisation here https://gitlab.com/hepcedar/contur/-/commit/c6d269614b3a1a07ecfe115170e618db8e9592bb. Note this commit is still in seperate branch yet to be merge with main.
