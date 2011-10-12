OpenErp Console:
--------------------

This is a module to be able to use the normal orm syntaxis from a console with to test the code without have to
restart the server

THIS IS BETA SOFTWARE

How to install?
---------------------------

1. Install [Cython] 
2. Install the [rfoo](http://code.google.com/p/rfoo/) note:dont use pip
   for this
3. Clone the repository on your openerp addons folder
3. Update you addons list in your openerp
4. Install the module in your project

How to use?
--------------------
This is still beta is the first version so this will change pretty soon.

1. Access to the project.
2. Launch rconsole
3. In the console there's 3 variable (\_self, \_uid, \_cr) which each correspond to self, cr, uid in the normal openerp functions

example of code:
<pre><code>
partners = _self.pool.get('res.partner')
partner = partners.browse(_cr, _uid, [1,2,3])
</code></pre>

