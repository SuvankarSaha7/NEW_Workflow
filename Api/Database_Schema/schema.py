from pydantic import BaseModel , ConfigDict
from typing import Optional,List
from datetime import datetime

# Pydantic models define what data looks like going IN and OUT of the API 
# they are totally seperate from Sqlalchemy models

############################# COMPANY ##############################
class COMPANY_CREATE(BaseModel):

    COMP_NAME: str
    COMP_CODE: str
    STATUS: Optional[int] = 1
    CREATED_BY: Optional[str] = None
    MODIFIED_BY: Optional[str] = None

class COMPANY_RESPONSE(BaseModel):

    COMP_ID: int
    COMP_NAME: str
    COMP_CODE: str
    STATUS : Optional[int]
    CREATED_AT: Optional[datetime]
    CREATED_BY: Optional[str]
    MODIFIED_AT: Optional[datetime]
    MODIFIED_BY:Optional[str]

    #  COMPANY_RESPONSE uses DIVISION_RESPONSE before it's defined, for that we need to start the code
    DIVISONS : Optional[List["DIVISION_RESPONSE"]] = []
    LEVELS : Optional[List["LEVEL_RESPONSE"]] = []
    GRADES: Optional[List["GRADE_RESPONSE"]] = []
    LEVEL_GRADES :Optional[List["LEVEL_GRADE_RESPONSE"]] =[]
    SAMPLING_ENTITLEMENT : Optional[List["SAMPLING_ENTITLEMENT_RESPONSE"]]

    model_config = ConfigDict(from_attributes=True)

########################## DIVISION ################################

class DIVISION_CREATE(BaseModel):

    DIV_NAME: str
    DIV_CODE: str
    STATUS:Optional[int] = 1
    CREATED_BY : Optional[str] = None
    MODIFIED_BY: Optional[str] = None
    COMP_ID: int  # which company this division belongs to


class DIVISION_RESPONSE(BaseModel):

    DIV_ID: int
    DIV_NAME:str
    DIV_CODE:str
    STATUS: Optional[int]
    CREATED_AT: Optional[datetime]
    CREATED_BY: Optional[str]
    MODIFIED_AT: Optional[datetime]
    MODIFIED_BY:Optional[str]
    COMP_ID:int

    model_config = ConfigDict(from_attributes=True)


########################### LEVEL ##########################################

class LEVEL_CREATE(BaseModel):

    LVL_NAME:str
    LVL_CODE:str
    STATUS:Optional[int] = 1
    CREATED_BY:Optional[str] = None
    MODIFIED_BY: Optional[str] = None
    COMP_ID :int
    
class LEVEL_RESPONSE(BaseModel):

    LVL_ID: int
    LVL_NAME:str
    LVL_CODE:str
    STATUS: Optional[int]
    CREATED_AT:Optional[datetime]
    CREATED_BY:Optional[str]
    MODIFIED_AT:Optional[datetime]
    MODIFIED_BY:Optional[str]
    COMP_ID:int


    model_config = ConfigDict(from_attributes=True)


########################### GRADE ##########################################

class GRADE_CREATE(BaseModel):

    GRD_NAME:str
    GRD_CODE:str
    STATUS:Optional[int] = 1
    CREATED_BY:Optional[str] = None
    MODIFIED_BY: Optional[str] = None
    COMP_ID :int
    
class GRADE_RESPONSE(BaseModel):

    GRD_ID: int
    GRD_NAME:str
    GRD_CODE:str
    STATUS: Optional[int]
    CREATED_AT:Optional[datetime]
    CREATED_BY:Optional[str]
    MODIFIED_AT:Optional[datetime]
    MODIFIED_BY:Optional[str]
    COMP_ID:int



    model_config = ConfigDict(from_attributes=True)

########################### LEVEL_GRADE ##########################################
    
class LEVEL_GRADE_CREATE(BaseModel):
    
    STATUS:Optional[int] = 1
    CREATED_BY:Optional[str] = None
    MODIFIED_BY: Optional[str] = None
    COMP_ID :int
    DIV_ID: int
    LVL_ID : int
    GRD_ID : int
    
class LEVEL_GRADE_RESPONSE(BaseModel):

    LVL_GRD_ID: int
    STATUS: Optional[int]
    CREATED_AT:Optional[datetime]
    CREATED_BY:Optional[str]
    MODIFIED_AT:Optional[datetime]
    MODIFIED_BY:Optional[str]
    COMP_ID:int
    DIV_ID: int
    LVL_ID : int
    GRD_ID : int


    model_config = ConfigDict(from_attributes=True)

################################### SAMPLING ENTITLEMENT #######################################

class SAMPLING_ENTITLEMENT_CREATE(BaseModel):

    SAMP_AMOUNT:int
    STATUS:Optional[int] = 1
    CREATED_BY:Optional[str] = None
    MODIFIED_BY: Optional[str] = None
    LVL_GRD_ID: int
    
class SAMPLING_ENTITLEMENT_RESPONSE(BaseModel):
    SAMP_ENT_ID: int
    SAMP_AMOUNT: int
    STATUS: Optional[int]
    CREATED_AT:Optional[datetime]
    CREATED_BY:Optional[str]
    MODIFIED_AT:Optional[datetime]
    MODIFIED_BY:Optional[str]
    LVL_GRD_ID : int


    model_config = ConfigDict(from_attributes=True)
    


COMPANY_RESPONSE.model_rebuild()