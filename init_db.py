from app import create_app, db
from app.models import User, Department, House, InventoryItem, InventoryRequest, RepairRequest, PurchasePlan, Event

app = create_app()

with app.app_context():
    # Создаем все таблицы
    db.create_all()

    # Создаем администратора
    if not User.query.filter_by(role='admin').first():
        admin = User(
            username='admin',
            email='admin@example.com',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)

    # Создаем 3 дома
    if not House.query.first():
        houses = [
            House(name='Дом 1', address='Адрес 1', capacity=10),
            House(name='Дом 2', address='Адрес 2', capacity=8),
            House(name='Дом 3', address='Адрес 3', capacity=12)
        ]
        db.session.add_all(houses)

    db.session.commit()
    print("База данных успешно инициализирована!")