"""Очищает таблицы defects и employees."""
from ORM import MyORM

MyORM.delete('defects')
MyORM.delete('employees')
