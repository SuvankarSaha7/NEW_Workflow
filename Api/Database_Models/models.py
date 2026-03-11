from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from Database.db import Base


class COMPANY_MASTER_MODEL(Base):
    __tablename__ = "COMPANY_MASTER"

    COMP_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    COMP_NAME= Column( String(50),nullable=False)
    COMP_CODE = Column( String(50),nullable=False)
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime, server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime)
    MODIFIED_BY=Column(String(100))

    DIVISONS = relationship("DIVISION_MASTER_MODEL",back_populates="COMPANY")
    LEVELS = relationship("LEVEL_MASTER_MODEL",back_populates="COMPANY")
    GRADES = relationship("GRADE_MASTER_MODEL",back_populates="COMPANY")
    LEVEL_GRADES= relationship("LEVEL_GRADE_MAPPING_MASTER_MODEL",back_populates="COMPANY")





####################################################################################

class DIVISION_MASTER_MODEL(Base):
    __tablename__ = "DIVISION_MASTER"

    DIV_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    DIV_NAME= Column( String(50),nullable=False)
    DIV_CODE = Column( String(50),nullable=False)
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime,server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime,onupdate=func.now())
    MODIFIED_BY=Column(String(100))

    COMP_ID = Column(Integer,ForeignKey("COMPANY_MASTER.COMP_ID"))
    COMPANY = relationship("COMPANY_MASTER_MODEL",back_populates="DIVISONS")



##########################################################################

class LEVEL_MASTER_MODEL(Base):
    __tablename__ = "LEVEL_MASTER"

    LVL_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    LVL_NAME= Column( String(50),nullable=False)
    LVL_CODE = Column( String(50),nullable=False)
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime,server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime,onupdate=func.now())
    MODIFIED_BY=Column(String(100))

    COMP_ID = Column(Integer,ForeignKey("COMPANY_MASTER.COMP_ID"))

    COMPANY=relationship("COMPANY_MASTER_MODEL",back_populates="LEVELS")
    LEVEL_GRADES = relationship("LEVEL_GRADE_MAPPING_MASTER_MODEL",back_populates="LEVEL")



###########################################################################################



class GRADE_MASTER_MODEL(Base):
    __tablename__ = "GRADE_MASTER"

    GRD_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    
    GRD_NAME= Column( String(50),nullable=False)
    GRD_CODE = Column( String(50),nullable=False)
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime,server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime,onupdate=func.now())
    MODIFIED_BY=Column(String(100))


    COMP_ID = Column(Integer, ForeignKey("COMPANY_MASTER.COMP_ID"))

    COMPANY = relationship("COMPANY_MASTER_MODEL",back_populates="GRADES")
    LEVEL_GRADES = relationship("LEVEL_GRADE_MAPPING_MASTER_MODEL",back_populates="GRADE")


#######################################################################################


class LEVEL_GRADE_MAPPING_MASTER_MODEL(Base):
    __tablename__ = "LEVEL_GRADE_MAPPING_MASTER"

    LVL_GRD_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime,server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime,onupdate=func.now())
    MODIFIED_BY=Column(String(100))


    COMP_ID = Column(Integer,ForeignKey("COMPANY_MASTER.COMP_ID"))
    DIV_ID= Column(Integer, ForeignKey("DIVISION_MASTER.DIV_ID"))
    LVL_ID = Column(Integer, ForeignKey("LEVEL_MASTER.LVL_ID"))
    GRD_ID = Column(Integer, ForeignKey("GRADE_MASTER.GRD_ID"))


    COMPANY = relationship("COMPANY_MASTER_MODEL",back_populates="LEVEL_GRADES")
    LEVEL=relationship("LEVEL_MASTER_MODEL",back_populates="LEVEL_GRADES")
    GRADE = relationship("GRADE_MASTER_MODEL",back_populates="LEVEL_GRADES")
    SAMPLING_ENT = relationship("SAMPLING_ENTITLEMENT_MASTER_MODEL",back_populates="LVL_GRADES")




##########################################################################################




class SAMPLING_ENTITLEMENT_MASTER_MODEL(Base):
    __tablename__ = "SAMPLING_ENTITLEMENT_MASTER"

    SAMP_ENT_ID= Column(Integer,primary_key=True,index=True,autoincrement=True)
    
    SAMP_AMOUNT=Column( String(50),nullable=False)
    STATUS = Column(Integer,default=1)
    CREATED_AT= Column(DateTime,server_default=func.now())
    CREATED_BY=Column(String(100))
    MODIFIED_AT=Column(DateTime,onupdate=func.now())
    MODIFIED_BY=Column(String(100))


    LVL_GRD_ID= Column(Integer,ForeignKey("LEVEL_GRADE_MAPPING_MASTER.LVL_GRD_ID"))
    
    LVL_GRADES = relationship("LEVEL_GRADE_MAPPING_MASTER_MODEL",back_populates="SAMPLING_ENT")


        




# variable_name = relationship("ModelClassName", back_populates="variable_in_other_model")
#    ↑                              ↑                               ↑
# how you access it          CLASS name of               must match variable name
# in your code               related model               defined in the other model