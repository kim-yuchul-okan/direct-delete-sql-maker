import lib.db as DB
import lib.definition as d


conn = DB.getConn('root', '', 'localhost', 'subsystem')
cur = conn.cursor()
key = d.Keys


def getRows(sql):
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) < 1:
        return ((None,),)
    return rows


def putSql(sqlArr):
    print("=========================")
    print("working sql")
    print("=========================")
    for sql in sqlArr:
        print(sql + ";")
        print(sql.replace('SELECT *', 'DELETE') + ";")
        print(sql + ";")


def dryPutSql(sqlArr):
    new_sql = []
    for sql in sqlArr:
        sql = sql.replace("None", "'None'")
        cur.execute(sql)
        rows = cur.fetchall()
        print(f"rows: {len(rows)}")
        if len(rows) > 0:
            print(f"ok -> {sql}")
            new_sql.append(sql)
        else:
            print(f"ng -> {sql}")

    print(new_sql)
    return new_sql


def existCompany():
    sql = f"SELECT company_id FROM `companies` WHERE company_id = {key['companyId']}"
    companyId = getRows(sql)[0][0]
    return companyId == key['companyId']


def setKey():
    sql = f"SELECT contact_id FROM contacts WHERE company_id = {key['companyId']}"
    key['contactId'] = getRows(sql)[0][0]

    sql = f"""
        SELECT contract_id FROM contracts WHERE company_id = {key['companyId']}
        UNION
        SELECT contract_id FROM tmp_contracts WHERE company_id = {key['companyId']}"""
    key['contractId'] = getRows(sql)[0][0]

    if key['contractId'] is not None:
        sql = f"""
            SELECT box_id FROM boxes WHERE contract_id = {key['contractId']}
            UNION
            SELECT box_id FROM tmp_boxes WHERE contract_id = {key['contractId']}"""
        key['boxId'] = getRows(sql)[0][0]

        sql = f"SELECT invoice_id FROM invoices WHERE contract_id = {key['contractId']}"
        key['invoiceId'] = getRows(sql)[0][0]

        sql = f"SELECT maintenance_schedule_id FROM maintenance_schedules WHERE contract_id = {key['contractId']}"
        key['maintenanceScheduleId'] = getRows(sql)[0][0]

        sql = f"SELECT * FROM `note_users` WHERE company_id = {key['companyId']} OR contract_id = {key['contractId']} OR contact_id = {key['contactId']};"
        key['noteUserId'] = getRows(sql)[0][0]

    if key['boxId'] is not None:
        sql = f"SELECT item_request_id FROM item_requests WHERE box_id = {key['boxId']}"
        key['invoiceId'] = getRows(sql)[0][0]
        sql = f"SELECT maintenance_id FROM box_maintenances WHERE box_id = {key['boxId']}"
        key['maintenanceId'] = getRows(sql)[0][0]

    print(key)


def main():
    key['companyId'] = 3147
    companyExist = existCompany()
    if not companyExist:
        DB.db_close(cur, conn)
        exit()

    setKey()
    new_sql = dryPutSql(d.make_sql(key))
    putSql(new_sql)

    DB.db_close(cur, conn)


main()