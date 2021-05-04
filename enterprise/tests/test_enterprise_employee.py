import unittest
from odoo.tests.common import TransactionCase
import datetime


class TestEnterpriseEmployee(TransactionCase):
    def setUp(self):
        super(TestEnterpriseEmployee, self).setUp()
        self.enterprise_client = self.env['enterprise.client'].create({
            'f_name': 'f_name',
            'l_name': 'l_name'
        })
        self.enterprise_department = self.env['enterprise.department'].create({
            'name': 'name',
            'code_dep': 'code_dep'
        })
        self.enterprise_job = self.env['enterprise.job'].create({
            'name': 'name'
        })

    def test_enterprise_employee(self):
        data = self.env['enterprise.employee'].create({
            'l_name': 'l_name',
            'f_name': 'f_name',
            'date_start': '2021-05-04',
            'department_id': self.enterprise_department.id,
            'job_uid': self.enterprise_job.id,
            'client_uid': self.enterprise_client.ids,
        })
        self.assertEqual(data.l_name, 'l_name')
        self.assertEqual(data.f_name, 'f_name')
        print(datetime.date.today())
        self.assertEqual(data.date_start, datetime.date(2021, 5, 4))
        self.assertEqual(data.department_id, self.enterprise_department)
        self.assertEqual(data.job_uid, self.enterprise_job)
