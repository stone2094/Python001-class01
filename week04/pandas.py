import pandas as pd
import numpy as np


#data = pd.DataFrame({'id':np.arange(1,20),'age':np.random.randint(10,1)})
#table1 = pd.DataFrame({'id':np.arange(1,10),'age':np.random.randint(30,1)})
#table2 = pd.DataFrame({'id':np.arange(1,10),'age':np.random.randint(40,10)})
#df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))

df = pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 

# SELECT * FROM data;
	
print(data)

# SELECT * FROM data LIMIT 10;
	
print(data.loc[ 0:9 ])
	
# SELECT id FROM data;  //id 是 data 表的特定一列
	
print(data[ [id] ])
	
# SELECT COUNT(id) FROM data;

did = data[[id]]	
did_count = did.count
print(did_count)
	
# SELECT * FROM data WHERE id<1000 AND age>30;
	
print(data.query(' (id < 1000) & (age >30)'))
	
# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
	
print(table1.drop_duplicates('order_id').groupby('id').count())
	
# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
	
print(pd.merge(table1, table2,how='inner', on=['id', 'id'])
	
# SELECT * FROM table1 UNION SELECT * FROM table2;
	
#way1
union_table = [ table1, table2 ]
unioned_table1 = pd.concat(union_table)
print(unioned_table1)
#way2
unioned_table2 = table1.append(table2)
print(unioned_table2)

# DELETE FROM table1 WHERE id=10;
	
drop_id_10 = table1[ table1['id'] == 10].index
table_delete = table1.drop(drop_id_10)
print(table_delete)
	
# ALTER TABLE table1 DROP COLUMN column_name;
# ALTER TABLE table1 DROP COLUMN id;
alter_table = table1.drop(columns=['id'] , axis=1)
print('alter_table')

