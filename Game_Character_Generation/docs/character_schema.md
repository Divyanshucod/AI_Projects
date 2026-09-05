## Every Character Boiler Plate

* CharacterId: String : required
* Name : String : required
* Personality : String : required
* Role : String : required
* Alignment : enums[Protagonist | Antagonist | Netural] required
* Gender : enum['Male','Female','Others'] : constraints (Only One Can be choosen)
* Physique :  free_form
* Supportive_Characters : ["CharacterId"] : Optional
* RelationShips : [{"characterId":String , relationship:String}] : Optional
* Strengths : List[String] : Constraints (At least One)
* Weeknesses : List[String] : Constraints (At least One)

## Validation
CharacterId Can not be duplicate
CharacterId Should be UUID
Name should atleast have three characters
Personality should be string and can't have only space or empty
Role should be string and can't be empty or can't have only spaces and tabs
aligntment should of any of these three Protagonist | Antagonist | Netural
gender only one can be choosen in these ['Male', 'Female',]
All the required fields should be present [CharacterId , Name, Personality, Role, Alignment, Gender, strengths, weeknesses]
Extra fields are invalid
Duplicate RelationShips are invalid
Empty Strengths are not allowed
Empty Weeknesses are not allowed