from pydantic import BaseModel


class ThemeOuvrageSchema(BaseModel):
    id_ouvrage: int
    id_theme: int

    class Config:
        from_attributes = True


class ThemeOuvrageSchemaOut(ThemeOuvrageSchema):
    nom_theme: str
