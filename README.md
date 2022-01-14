# direct-delete-sql-maker

## 環境

- MacOS Big Sur
- Python 3.7.12
- MySQL 5.6

## setup

- clone
  ```sh
  git clone https://github.com/kim-yuchul-okan/direct-delete-sql-maker.git
  ```
- library install
  ```sh
  pip install mysqlclient
  ```
- [db.py](./lib/db.py) ７行目にてローカル環境の`mysql.sock`の Path を合わせてください。
  ```py
  # mysql.sockのPath
  unix_socket='/tmp/mysql.sock',
  ```
- [make_delete_company.py](./make_delete_company.py) ５行目にてローカル環境の DB 接続環境を合わせてください。
  ```py
  # getConn({DB User Name}, '{DB User Password}', '{DB Host}', '{DB Name}')
  conn = DB.getConn('root', '', 'localhost', 'subsystem')
  ```

## Usage

- Usage

  ```sh
  python src/make_delete_company.py {company_id}
  ```

- 例

  - ターミナルで実行したら、以下のように表示されます。
  - `working sql`以下の SQL が対象のものになります。
  - `[確認必要]`が付けられた SQL は、別途で確認してください。怪しいものなので

  ```sh
  $ python src/make_delete_company.py "XXXX"
  {'companyId': XXXX, 'contactId': XXXXXX, 'contractId': XXXX, 'boxId': XXXX00, 'itemRequestId': None, 'maintenanceScheduleId': None, 'invoiceId': None, 'maintenanceId': None, 'noteUserId': XXXXXXX}
  rows: 1
  ok -> SELECT * FROM `companies` WHERE company_id = XXXX
  rows: 0
  ng -> SELECT * FROM `company_extents` WHERE company_id = XXXX
  rows: 1
  ok -> SELECT * FROM `contacts` WHERE company_id = XXXX
  rows: 0
  ng -> SELECT * FROM `contracts` WHERE company_id = XXXX
  rows: 1
  ok -> SELECT * FROM `tmp_contracts` WHERE company_id = XXXX
  ... 略 ...
  ['SELECT * FROM `companies` WHERE company_id = XXXX', 'SELECT * FROM `contacts` WHERE company_id = XXXX', 'SELECT * FROM `tmp_contracts` WHERE company_id = XXXX',  ... 略 ... ]
  =========================
  working sql
  =========================
  SELECT * FROM `companies` WHERE company_id = XXXX;
  DELETE FROM `companies` WHERE company_id = XXXX;
  SELECT * FROM `companies` WHERE company_id = XXXX;
  SELECT * FROM `contacts` WHERE company_id = XXXX;
  DELETE FROM `contacts` WHERE company_id = XXXX;
  SELECT * FROM `contacts` WHERE company_id = XXXX;
  SELECT * FROM `tmp_contracts` WHERE company_id = XXXX;
  DELETE FROM `tmp_contracts` WHERE company_id = XXXX;
  SELECT * FROM `tmp_contracts` WHERE company_id = XXXX;
  ... 略 ...
  [確認必要] SELECT * FROM `invoice_details` WHERE invoice_id = 'None';
  [確認必要] DELETE FROM `invoice_details` WHERE invoice_id = 'None';
  [確認必要] SELECT * FROM `invoice_details` WHERE invoice_id = 'None';
  $
  ```
