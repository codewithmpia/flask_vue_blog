from flask_admin import form 
from flask_admin.contrib.sqla import ModelView

from .settings import BASE_DIR

class PostAdminView(ModelView):
    form_extra_fields = {
        "image": form.ImageUploadField(
            label="Image",
            base_path=BASE_DIR / "frontend/src/assets/images"
        )
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model, is_created)
    

class ContactAdminView(ModelView):
    pass