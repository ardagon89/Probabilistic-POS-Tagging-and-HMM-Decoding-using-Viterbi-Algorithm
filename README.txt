Execute: python POS.py <filename <Algo_code Sentence>>

- Both filename and <Algo_code Sentence> are optional parameters and can be omitted. In that case the input filename is hardcoded in the program.
- If filename is passed as argument to the program the file should be in the same folder as the POS.py file.
- If <Algo_code Sentence> is passed along with the filename as an argument to the program, then only NB and HMM are the valid values for Algo_code.
- Sentence should in quotes.
- Observation_Table.csv and Transition_Table.csv are included in the archive. They should be present in the same folder for HMM Viterbi algo.

smoothing_code can take the following values:
NB : Naive Bayes Algorithm
HMM : HMM Viterbi Algorithm

#######################################################################################################################################################
Example 1: python POS.py

Output :

Naive Bayes Classification:
('John', 'NNP') 0.0010688042752171009
('NNP', '<s>')  0.23468468468468467
('went', 'VBD') 0.008768084173608066
('VBD', 'NNP')  0.07201068804275217
('to', 'TO')    0.9935525467440361
('TO', 'VBD')   0.06269180184129768
('work', 'VB')  0.0035035035035035035
('VB', 'TO')    0.63571889103804
('.', '.')      0.9920424403183024
('.', 'VB')     0.01901901901901902
('.', '</s>')   0.9473916887709991
John_NNP went_VBD to_TO work_VB ._.
The probability of the above sentence is : 3.927369866355776e-13
----------------------------------------------------------------------------------------------------
HMM Viterbi Algorithm:
                      Janet                    will                    back                     the                    bill
NNP              8.8544e-06                     0.0                     0.0   2.486139834207686e-17                     0.0
 MD                     0.0       3.00406859104e-08                     0.0                     0.0                     0.0
 VB                     0.0  2.2313087999999997e-13  1.6085273254449314e-11                     0.0  1.0170715811950793e-20
 JJ                     0.0                     0.0      5.106916604768e-15                     0.0                     0.0
 NN                     0.0          1.03419392e-10    5.35925836641536e-15                     0.0   2.013570710221386e-15
 RB                     0.0                     0.0  5.3284089852402517e-11                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.8161992521340703e-12                     0.0
The probability of the below POS sequence is : 2.013570710221386e-15
Janet_NNP will_MD back_VB the_DT bill_NN

                       will                   Janet                    back                     the                    bill
NNP                     0.0          4.73750016e-12                     0.0  1.4537573338978714e-22                     0.0
 MD  0.00018505859999999998                     0.0                     0.0                     0.0                     0.0
 VB                8.68e-08                     0.0  2.8652400967679996e-18                     0.0   6.046454487031505e-26
 JJ                     0.0                     0.0      1.353030045696e-17                     0.0                     0.0
 NN                8.98e-06                     0.0   6.169741208371199e-17                     0.0  1.1970606475374611e-20
 RB                     0.0                     0.0     4.4539134004224e-16                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.0797240155413401e-17                     0.0
The probability of the below POS sequence is : 1.1970606475374611e-20
will_MD Janet_NNP back_RB the_DT bill_NN

                       back                     the                    bill                   Janet                    will
NNP                     0.0  1.7388829439999998e-10                     0.0   4.398613413942791e-15                     0.0
 MD                     0.0                     0.0                     0.0                     0.0   1.492335607263368e-17
 VB              2.0832e-06                     0.0   7.232346371715695e-14                     0.0  1.1084505803135833e-22
 JJ  1.5402000000000003e-05                     0.0                     0.0                     0.0                     0.0
 NN             1.00127e-05                     0.0  1.4318403040178357e-08                     0.0    5.13758046748518e-20
 RB             0.000532746                     0.0                     0.0                     0.0                     0.0
 DT                     0.0  1.2914904235206597e-05                     0.0                     0.0                     0.0
The probability of the below POS sequence is : 1.492335607263368e-17
back_RB the_DT bill_NN Janet_NNP will_MD

#######################################################################################################################################################
Example 2: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt

Output : 

Naive Bayes Classification:
('John', 'NNP') 0.0010688042752171009
('NNP', '<s>')  0.23468468468468467
('went', 'VBD') 0.008768084173608066
('VBD', 'NNP')  0.07201068804275217
('to', 'TO')    0.9935525467440361
('TO', 'VBD')   0.06269180184129768
('work', 'VB')  0.0035035035035035035
('VB', 'TO')    0.63571889103804
('.', '.')      0.9920424403183024
('.', 'VB')     0.01901901901901902
('.', '</s>')   0.9473916887709991
John_NNP went_VBD to_TO work_VB ._.
The probability of the above sentence is : 3.927369866355776e-13
----------------------------------------------------------------------------------------------------
HMM Viterbi Algorithm:
                      Janet                    will                    back                     the                    bill
NNP              8.8544e-06                     0.0                     0.0   2.486139834207686e-17                     0.0
 MD                     0.0       3.00406859104e-08                     0.0                     0.0                     0.0
 VB                     0.0  2.2313087999999997e-13  1.6085273254449314e-11                     0.0  1.0170715811950793e-20
 JJ                     0.0                     0.0      5.106916604768e-15                     0.0                     0.0
 NN                     0.0          1.03419392e-10    5.35925836641536e-15                     0.0   2.013570710221386e-15
 RB                     0.0                     0.0  5.3284089852402517e-11                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.8161992521340703e-12                     0.0
The probability of the below POS sequence is : 2.013570710221386e-15
Janet_NNP will_MD back_VB the_DT bill_NN

                       will                   Janet                    back                     the                    bill
NNP                     0.0          4.73750016e-12                     0.0  1.4537573338978714e-22                     0.0
 MD  0.00018505859999999998                     0.0                     0.0                     0.0                     0.0
 VB                8.68e-08                     0.0  2.8652400967679996e-18                     0.0   6.046454487031505e-26
 JJ                     0.0                     0.0      1.353030045696e-17                     0.0                     0.0
 NN                8.98e-06                     0.0   6.169741208371199e-17                     0.0  1.1970606475374611e-20
 RB                     0.0                     0.0     4.4539134004224e-16                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.0797240155413401e-17                     0.0
The probability of the below POS sequence is : 1.1970606475374611e-20
will_MD Janet_NNP back_RB the_DT bill_NN

                       back                     the                    bill                   Janet                    will
NNP                     0.0  1.7388829439999998e-10                     0.0   4.398613413942791e-15                     0.0
 MD                     0.0                     0.0                     0.0                     0.0   1.492335607263368e-17
 VB              2.0832e-06                     0.0   7.232346371715695e-14                     0.0  1.1084505803135833e-22
 JJ  1.5402000000000003e-05                     0.0                     0.0                     0.0                     0.0
 NN             1.00127e-05                     0.0  1.4318403040178357e-08                     0.0    5.13758046748518e-20
 RB             0.000532746                     0.0                     0.0                     0.0                     0.0
 DT                     0.0  1.2914904235206597e-05                     0.0                     0.0                     0.0
The probability of the below POS sequence is : 1.492335607263368e-17
back_RB the_DT bill_NN Janet_NNP will_MD

#######################################################################################################################################################
Example 3: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt NB "John went to work ."

Output : 

('John', 'NNP') 0.0010688042752171009
('NNP', '<s>')  0.23468468468468467
('went', 'VBD') 0.008768084173608066
('VBD', 'NNP')  0.07201068804275217
('to', 'TO')    0.9935525467440361
('TO', 'VBD')   0.06269180184129768
('work', 'VB')  0.0035035035035035035
('VB', 'TO')    0.63571889103804
('.', '.')      0.9920424403183024
('.', 'VB')     0.01901901901901902
('.', '</s>')   0.9473916887709991
John_NNP went_VBD to_TO work_VB ._.
The probability of the above sentence is : 3.927369866355776e-13

#######################################################################################################################################################
Example 4: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt HMM "Janet will back the bill"

Output : 

                      Janet                    will                    back                     the                    bill
NNP              8.8544e-06                     0.0                     0.0   2.486139834207686e-17                     0.0
 MD                     0.0       3.00406859104e-08                     0.0                     0.0                     0.0
 VB                     0.0  2.2313087999999997e-13  1.6085273254449314e-11                     0.0  1.0170715811950793e-20
 JJ                     0.0                     0.0      5.106916604768e-15                     0.0                     0.0
 NN                     0.0          1.03419392e-10    5.35925836641536e-15                     0.0   2.013570710221386e-15
 RB                     0.0                     0.0  5.3284089852402517e-11                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.8161992521340703e-12                     0.0
The probability of the below POS sequence is : 2.013570710221386e-15
Janet_NNP will_MD back_VB the_DT bill_NN

#######################################################################################################################################################
Example 5: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt HMM "will Janet back the bill"

Output:

                       will                   Janet                    back                     the                    bill
NNP                     0.0          4.73750016e-12                     0.0  1.4537573338978714e-22                     0.0
 MD  0.00018505859999999998                     0.0                     0.0                     0.0                     0.0
 VB                8.68e-08                     0.0  2.8652400967679996e-18                     0.0   6.046454487031505e-26
 JJ                     0.0                     0.0      1.353030045696e-17                     0.0                     0.0
 NN                8.98e-06                     0.0   6.169741208371199e-17                     0.0  1.1970606475374611e-20
 RB                     0.0                     0.0     4.4539134004224e-16                     0.0                     0.0
 DT                     0.0                     0.0                     0.0  1.0797240155413401e-17                     0.0
The probability of the below POS sequence is : 1.1970606475374611e-20
will_MD Janet_NNP back_RB the_DT bill_NN

#######################################################################################################################################################
Example 6: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt HMM "back the bill Janet will"

Output : 

                       back                     the                    bill                   Janet                    will
NNP                     0.0  1.7388829439999998e-10                     0.0   4.398613413942791e-15                     0.0
 MD                     0.0                     0.0                     0.0                     0.0   1.492335607263368e-17
 VB              2.0832e-06                     0.0   7.232346371715695e-14                     0.0  1.1084505803135833e-22
 JJ  1.5402000000000003e-05                     0.0                     0.0                     0.0                     0.0
 NN             1.00127e-05                     0.0  1.4318403040178357e-08                     0.0    5.13758046748518e-20
 RB             0.000532746                     0.0                     0.0                     0.0                     0.0
 DT                     0.0  1.2914904235206597e-05                     0.0                     0.0                     0.0
The probability of the below POS sequence is : 1.492335607263368e-17
back_RB the_DT bill_NN Janet_NNP will_MD

#######################################################################################################################################################
Example 7: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt X "back the bill Janet will"

Output : 

Enter correct input
#######################################################################################################################################################
Example 8: python POS.py NLP6320_POSTaggedTrainingSet-Windows.txt Y

Output : 

Enter correct input
