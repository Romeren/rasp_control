from RaspBoard.a_service import RestHandler as superClass
import os

class Service(superClass):
    def initialize(self, module):
        self.module = module
        self.key_file = module.virtual_dir + '/' + ".controllcenter"

    def get(self):
        context = self.get_basic_context(config)

        res = """
            <input id="username" type="text" placeholder="Username" name="usr"/>
            <input id="password" type="password" placeholder="Password" name="pwrd"/>
            <input type="button" name="submit" value="Login" onclick="submitLogin()"/>
            <script>
                function submitLogin(){
                    var usr = document.getElementById('username').value;
                    var pass = document.getElementById('password').value;
                    var data = {
                        'username': usr,
                        'password': pass
                    };
                    data = JSON.stringify(data);
                    var url = "{{ context.references.self.address }}";

                    var httpRequest = new XMLHttpRequest();
                    httpRequest.onreadystatechange = function (data) {
                        // code for redir
                    }
                    httpRequest.setRequestHeader('Content-Type', 'application/json');
                    httpRequest.open('POST', url);
                    httpRequest.send(data);    
                }
            </script>
        """
        self.write(res)

    def post(self):

        success, cont = self.__get_content__(self.key_file)
        if(not success):
            # init
            return
        return

    def __get_content__(self, file_name):
        if(os.path.exists(file_name)):
            file = open(file_name, 'r')
            content = file.read()
            return True, content
        return False, None

config = {
    "service_name": "controll/login",
    "handler": Service,
    "service_type": "rest",
    "service_category": "system",
    "dependencies": []
}
