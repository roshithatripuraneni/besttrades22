# Investor SQL statements
investor_by_id = 'select name, address, status, id from investor where id = %s'
get_investors_by_name_sql = 'select name, address, status, id from investor where name = %s'
create_investor = 'insert into investor (name, address, status) values (%s, %s, %s)'
update_investor_name = 'update investor set name = %s where id = %s'
update_investor_address = 'update investor set address = %s where id = %s'