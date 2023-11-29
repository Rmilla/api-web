from pydantic import BaseModel


class ThemeSchema(BaseModel):
    theme_id: int
    nom_theme: str


class ThemeSchemaOut(ThemeSchema):
    pass
