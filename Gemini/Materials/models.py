from django.db import models

class Project(models.Model):
    project_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.FloatField()

class ItemGroup(models.Model):
    group_id = models.CharField(max_length=1, primary_key=True)
    format_rule_id = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

class ItemSubGroup(models.Model):
    category_id = models.CharField(max_length=3, primary_key=True)
    format_rule_id = models.IntegerField()
    group_id = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

class StorageArea(models.Model):
    storage_area_id = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()

class StorageLocation(models.Model):
    storage_location_id = models.CharField(max_length=10, primary_key=True)
    storage_area_id = models.ForeignKey(StorageArea, on_delete=models.CASCADE)

class Item(models.Model):
    item_number = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()
    unit = models.CharField(max_length=20)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    manual_id = models.IntegerField()
    state = models.CharField(max_length=50)
    storage_location_id = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)
    group_id = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    sub_group_id = models.ForeignKey(ItemSubGroup, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=50)
    assembly_time = models.FloatField()
    machine_time = models.FloatField()
    needs_time = models.BooleanField()
    needs_instructions = models.BooleanField()
    needs_sn = models.BooleanField()
    needs_lot_no = models.BooleanField()

class ItemBOM(models.Model):
    item_bom_id = models.IntegerField(primary_key=True)
    item_number = models.ForeignKey(Item, on_delete=models.CASCADE)
    used_item_number = models.CharField(max_length=20)
    quantity = models.FloatField()

class Manual(models.Model):
    manual_id = models.IntegerField(primary_key=True)
    text = models.TextField()
    tools = models.CharField(max_length=50)

class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

class ItemSupplier(models.Model):
    item_supplier_id = models.IntegerField(primary_key=True)
    item_number = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_item_number = models.CharField(max_length=50)
    supplier_description = models.TextField()
    price = models.FloatField()

class Tool(models.Model):
    tool_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    power = models.BooleanField()
    fixed = models.BooleanField()
    storage_location_id = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)

class FormatRule(models.Model):
    format_rule_id = models.IntegerField(primary_key=True)
    position_in_name = models.IntegerField()
    digits_number_start = models.IntegerField()
    digits_number_end = models.IntegerField()
    type = models

