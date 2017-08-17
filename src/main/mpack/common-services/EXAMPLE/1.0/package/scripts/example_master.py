from resource_management.core.logger import Logger
from resource_management.libraries.functions.check_process_status import check_process_status
from resource_management.libraries.functions.format import format
from resource_management.libraries.script.script import Script
from resource_management.core.resources.system import Directory, File, Execute
from resource_management.core.source import Template, InlineTemplate, DownloadSource

class ExampleMaster(Script):

    def install(self, env):
        '''
        File('/tmp/elasticsearch-2.4.4.tar.gz',
           content = DownloadSource(params.elasticsearch_download_url),
          mode = 0644
        )

        Execute(
          ('tar', 'zxvf', '/tmp/elasticsearch-2.4.4.tar.gz', '-C', '/opt/'),
          sudo=True
        )
        '''
        pass


    def configure(self, env):
        pass

    def start(self, env):
        '''
        Logger.info("Starting Elasticsearch ... ")
        start_command = format('{elasticsearch_home}/bin/elasticsearch -Des.node.name={node_name} -Des.node.master={isMaster} -Des.node.data={isData} -Des.http.port={port} -Des.path.data={path_data} -d -p {pid_file}')

        Execute(
                start_command,
                environment={
                   'JAVA_HOME': params.java64_home,
                   'ES_HEAP_SIZE': memory
                },
                user=params.elasticsearch_config_user
        )
        '''
        pass


    def stop(self, env):
        '''
        pid_file = config['pid_file']

        Execute(
                format('kill `cat {pid_file}`'),
                user=params.elasticsearch_config_user,
                only_if=format('test -f {pid_file}')
        )

        File(pid_file,
             action="delete"
        )
        '''
        pass

    def status(self, env):
        '''
        check_process_status(pid_file)
        '''
        pass

if __name__ == "__main__":
    ExampleMaster().execute()

