from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
(.venv) PS D:\python cache mohammadhosein zadeh\darmangah> python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlite3.IntegrityError: UNIQUE constraint failed: user.username

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\darmangah\app.py", line 17, in <module>
    db.session.commit()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
  File "<string>", line 2, in commit
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
  File "<string>", line 2, in _prepare_impl
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
             ^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
           ^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.username
[SQL: INSERT INTO user (username, password) VALUES (?, ?)]
[parameters: ('darmangeh', '12345678')]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
(.venv) PS D:\python cache mohammadhosein zadeh\darmangah> python app.py
Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlite3.IntegrityError: UNIQUE constraint failed: user.username

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\darmangah\app.py", line 17, in <module>
    db.session.commit()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
  File "<string>", line 2, in commit
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
  File "<string>", line 2, in _prepare_impl
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
             ^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
           ^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.username
[SQL: INSERT INTO user (username, password) VALUES (?, ?)]
[parameters: ('darmangeh', '12345678')]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
(.venv) PS D:\python cache mohammadhosein zadeh\darmangah> python app.py
Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlite3.IntegrityError: UNIQUE constraint failed: user.username

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\python cache mohammadhosein zadeh\darmangah\app.py", line 17, in <module>
    db.session.commit()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
  File "<string>", line 2, in commit
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
  File "<string>", line 2, in _prepare_impl
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
             ^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
           ^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "D:\python cache mohammadhosein zadeh\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.username
[SQL: INSERT INTO user (username, password) VALUES (?, ?)]
[parameters: ('darmangeh', '12345678')]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
(.venv) PS D:\python cache mohammadhosein zadeh\darmangah> 
