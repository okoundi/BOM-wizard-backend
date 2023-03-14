import random
from Materials.models import *
from faker import Faker
from random import randint
from django.utils import timezone

fake = Faker()

def generate_projects():
    projects = []
    for i in range(2000):
        project_id = f"P{i}"
        name = fake.company()
        description = fake.paragraph()
        start_date = fake.date_between(start_date='-2y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+1y')
        status = randint(0, 100)
        project = Project(project_id=project_id, name=name, description=description, start_date=start_date, end_date=end_date, status=status)
        projects.append(project)
    Project.objects.bulk_create(projects)

def generate_item_groups():
    item_groups = []
    for i in range(10):
        group_id = chr(ord('A') + i)
        format_rule_id = randint(1, 10)
        name = fake.word()
        description = fake.paragraph()
        item_group = ItemGroup(group_id=group_id, format_rule_id=format_rule_id, name=name, description=description)
        item_groups.append(item_group)
    ItemGroup.objects.bulk_create(item_groups)

def generate_item_subgroups():
    item_subgroups = []
    for i in range(10):
        category_id = f"CAT{i}"
        format_rule_id = randint(1, 10)
        group_id = ItemGroup.objects.order_by('?').first()
        name = fake.word()
        description = fake.paragraph()
        item_subgroup = ItemSubGroup(category_id=category_id, format_rule_id=format_rule_id, group_id=group_id, name=name, description=description)
        item_subgroups.append(item_subgroup)
    ItemSubGroup.objects.bulk_create(item_subgroups)

def generate_storage_areas():
    storage_areas = []
    for i in range(10):
        storage_area_id = f"SA{i}"
        description = fake.paragraph()
        storage_area = StorageArea(storage_area_id=storage_area_id, description=description)
        storage_areas.append(storage_area)
    StorageArea.objects.bulk_create(storage_areas)

def generate_storage_locations():
    storage_locations = []
    for i in range(10):
        storage_location_id = f"SL{i}"
        storage_area_id = StorageArea.objects.order_by('?').first()
        storage_location = StorageLocation(storage_location_id=storage_location_id, storage_area_id=storage_area_id)
        storage_locations.append(storage_location)
    StorageLocation.objects.bulk_create(storage_locations)

def generate_items():
    for i in range(50):
        item = Item(
            item_number=fake.ean13(),
            description=fake.text(),
            unit=fake.word(),
            project_id_id=random.randint(1, 10),
            manual_id_id=random.randint(1, 10),
            state=random.choice(['In Stock', 'Out of Stock']),
            storage_location_id_id=random.randint(1, 10),
            group_id_id=random.randint(1, 10),
            sub_group_id_id=random.randint(1, 10),
            item_type=random.choice(['Electronic', 'Mechanical']),
            assembly_time=random.uniform(0.5, 10),
            machine_time=random.uniform(0.5, 10),
            needs_time=fake.boolean(),
            needs_instructions=fake.boolean(),
            needs_sn=fake.boolean(),
            needs_lot_no=fake.boolean()
        )
        item.save()

# Generate item BOMs
def generate_item_boms():
    for i in range(50):
        item_bom = ItemBOM(
            item_bom_id=i+1,
            item_number_id=random.randint(1, 50),
            used_item_number=fake.ean13(),
            quantity=random.uniform(1, 10)
        )
        item_bom.save()

# Generate manuals
def generate_manuals():
    for i in range(10):
        manual = Manual(
            manual_id=i+1,
            text=fake.text(),
            tools=fake.word()
        )
        manual.save()

# Generate suppliers
def generate_suppliers():
    for i in range(10):
        supplier = Supplier(
            supplier_id=i+1,
            name=fake.company(),
            mail=fake.email(),
            phone=fake.phone_number(),
            website=fake.url(),
            customer_id=fake.ean13(),
            type=random.choice(['Manufacturer', 'Distributor'])
        )
        supplier.save()

# Generate item suppliers
def generate_item_suppliers():
    for i in range(50):
        item_supplier = ItemSupplier(
            item_supplier_id=i+1,
            item_number_id=random.randint(1, 50),
            supplier_id_id=random.randint(1, 10),
            supplier_item_number=fake.ean13(),
            supplier_description=fake.text(),
            price=random.uniform(0.5, 100)
        )
        item_supplier.save()

# Generate tools
def generate_tools():
    for i in range(10):
        tool = Tool(
            tool_id=i+1,
            name=fake.word() + ' ' + fake.word(),
            power=fake.boolean(),
            fixed=fake.boolean(),
            storage_location_id_id=random.randint(1, 10)
        )
        tool.save()

# Generate format rules
def generate_format_rules():
    for i in range(10):
        format_rule = FormatRule(
            format_rule_id=i+1,
            position_in_name=random.randint(1, 10),
            digits_number_start=random.randint(1, 10),
            digits_number_end=random.randint(1, 10),
            type=random.choice(['Prefix', 'Suffix'])
        )
        format_rule.save()


generate_projects()
generate_item_groups()
generate_item_subgroups()
generate_storage_areas()
generate_storage_locations()
generate_items()
generate_item_boms()
generate_manuals()
generate_suppliers()
generate_item_suppliers()
generate_tools()
generate_format_rules()
