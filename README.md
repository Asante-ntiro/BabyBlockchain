# BabyBlockchain-in-Haskell
A simple blockchain written in Haskell


## BLOCKCHAIN BASED VOTING SYSTEM
Here we have a blockchain based electronic voting system. Traditional electronic voting systems are both  easy to manipulate and hard to audit, using a solution based of blockchain technology would be able to solve this. Blockchain technologies bring Availability, Integrity and Confidentiality to the voting systems.

### OVERVIEW
The main purpose of the system is to attain the following:
#### ELIGIBILITY
  <sub>In this only legitmate voters will be able to participate in the election process</sub>
#### ONE VOTE PER PERSON
 <sub> Voters should not be able to participate in the process twice. You can participate once. </sub>
#### CONFIDENTIALITY
 <sub> Only a voter knows about the voters choice</sub>
#### NO ONE CAN OBTAIN INTERMEDIATE VOTING RESULTS
  <sub> The results will only be known after all votes are tallied  </sub> 
	
#### SYSTEM	BOUNDARIES
The verification of a voter's eligibility must be done by trusted organization or a decentralized I.D. (DIDs) system to verify the identity and eligibility of the participant. The system must also be able to tally the final result.

#### INTERACTIONS
The system should be integrated with national identification or a decentralized ID system (e.g. Atala Prism)

#### PRODUCT FEATURES 
The system should be able to fetch data from national identification system and in this case it should check the Date of birth of the participate and the nationality
The product must be able to verify the biometrical verification of the voter
After the vote is cast ,the voter should not be able to access the system to participate again , it should be able to identify if that particular participant has already participated in voting process
After all voting is done, the product must tally the results.

#### SECURITY REQUIREMENT.

 * Availability
 * Confidentiality
 * Integrity
 * Auditability

#### USER CHARACTERISTICS
 * Above 18 years old (subject to change based on specific countries' definition of Adult).
 * Citizens residing in the country where the election is being held.


	
 