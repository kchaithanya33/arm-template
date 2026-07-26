from pydantic import BaseModel



class DeleteRequest(BaseModel):

    subscription_id:str

    resource_group:str

    resource_name:str

    resource_type:str