import os
os.system('git bisect start c0e76c8eef27475fc58006a140886bf0bf512ac1 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect run python manage.py test')