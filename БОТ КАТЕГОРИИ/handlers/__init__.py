from aiogram import Router

from .user import router as user_router
from .categories import router as categories_router
from .faq import router as faq_router
from .contact import router as contact_router

def register_all_handlers(dp: Router):
    dp.include_router(user_router)
    dp.include_router(categories_router)
    dp.include_router(faq_router)
    dp.include_router(contact_router)
