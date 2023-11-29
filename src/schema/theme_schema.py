from pydantic import BaseModel


class ThemeSchema(BaseModel):
    theme_id: int
    nom_theme: str

    class Config:
        from_attributes = True


class ThemeSchemaOut(ThemeSchema):
    pass
