KeyTables = [
    "companies",
    "contacts",
    "contracts",
    "boxes",
    "invoices",
    "item_requests",
    "maintenance_schedules",
]
Keys = {
    "companyId": None,
    "contactId": None,
    "contractId": None,
    "boxId": None,
    "itemRequestId": None,
    "maintenanceScheduleId": None,
    "invoiceId": None,
    "maintenanceId": None,
    "noteUserId": None
}


def make_sql(key):
    return [
        f"SELECT * FROM `companies` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `company_extents` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `contacts` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `contracts` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `tmp_contracts` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `invoice_send_logs` WHERE company_id = {key['companyId']}",
        f"SELECT * FROM `mapping_companies_contacts` WHERE contact_id = {key['contactId']}",
        f"SELECT * FROM `note_users` WHERE company_id = {key['companyId']} OR contract_id = {key['contractId']} OR contact_id = {key['contactId']}",
        f"SELECT * FROM `application_send_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `auto_renewal_contracts_office_options` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `boxes` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `tmp_boxes` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_delivery_available_hours` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_delivery_dates` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_delivery_locations` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_delivery_okanbins` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_extents` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contract_sales_accumulations` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_cs_tags` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_addons` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_addons_histories` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_options` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_options_histories` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_plans` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_office_plans_histories` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `contracts_unreceivable_dates` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `demand_letter_send_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `invoice_detail_spots` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `invoice_note_templates` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `invoices` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `maintenance_schedules` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `mapping_contracts_addons` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `mapping_contracts_contacts` WHERE contract_id = {key['contractId']} OR contact_id = {key['contactId']}",
        f"SELECT * FROM `mapping_contracts_note_restrictable_functions` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `mapping_contracts_plans` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `mapping_note_users_note_roles` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `box_achievements` WHERE maintenance_id = {key['maintenanceId']}",
        f"SELECT * FROM `box_maintenance_extents` WHERE maintenance_id = {key['maintenanceId']}",
        f"SELECT * FROM `box_orders` WHERE maintenance_id = {key['maintenanceId']}",
        f"SELECT * FROM `box_payments` WHERE maintenance_id = {key['maintenanceId']}",
        f"SELECT * FROM `box_stocks` WHERE maintenance_id = {key['maintenanceId']}",
        f"SELECT * FROM `box_continuous_request_shots` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `box_continuous_requests` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `box_maintenances` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `box_offsets` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `box_prepares` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `boxes_control_numbers` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `item_continuous_request_shots` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `item_continuous_requests` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `item_requests` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `maintenance_schedule_extents` WHERE maintenance_schedule_id = {key['maintenanceScheduleId']} OR box_id = {key['boxId']}",
        f"SELECT * FROM `material_continuous_request_shots` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `material_continuous_requests` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `material_requests` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `note_maintenances` WHERE box_id = {key['boxId']}",
        f"SELECT * FROM `invoice_details` WHERE invoice_id = {key['invoiceId']}",
        f"SELECT * FROM `invoice_notes` WHERE invoice_id = {key['invoiceId']}",
        f"SELECT * FROM `invoice_payments` WHERE invoice_id = {key['invoiceId']}",
        f"SELECT * FROM `invoice_send_log_details` WHERE invoice_id = {key['invoiceId']}",
        f"SELECT * FROM `item_request_extents` WHERE item_request_id = {key['itemRequestId']}",
        f"SELECT * FROM `maintenance_schedule_available_hours` WHERE maintenance_schedule_id = {key['maintenanceScheduleId']}",
        f"SELECT * FROM `office_addon_order_send_logs` WHERE office_addon_order_id IN(SELECT office_addon_order_id FROM office_addon_orders WHERE contract_id = {key['contractId']})",
        f"SELECT * FROM `office_addon_orders` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `office_plan_order_send_logs` WHERE office_plan_order_id IN(SELECT `office_plan_order_id` FROM office_plan_orders WHERE contract_id = {key['contractId']})",
        f"SELECT * FROM `office_plan_orders` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `plan_revision_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `plan_revision_send_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `schedule_adjustment_requests` WHERE contract_id = {key['contractId']} OR note_user_id = {key['noteUserId']}",
        # f"SELECT * FROM `schedule_mail_send_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `statement_of_delivery_send_log_details` WHERE statement_of_delivery_send_log_id in (SELECT statement_of_delivery_send_log_id FROM `statement_of_delivery_send_logs` WHERE contract_id = {key['contractId']})",
        f"SELECT * FROM `statement_of_delivery_send_logs` WHERE contract_id = {key['contractId']}",
        f"SELECT * FROM `tft_donation_requests` WHERE contract_id = {key['contractId']}",
    ]
