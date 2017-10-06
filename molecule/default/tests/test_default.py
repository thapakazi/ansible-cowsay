import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_cowsay_installed(Package):
    p = Package('cowsay')
    assert p.is_installed


def test_if_cow_can_speak(Command):
    expected = (' __________________\n'
                '< hello test infra >\n'
                ' ------------------\n'
                '        \\   ^__^\n'
                '         \\  (oo)\\_______\n'
                '            (__)\\       )\\/\\\n'
                '                ||----w |\n'
                '                ||     ||')

    c = Command('export PATH=$PATH:/usr/games/ && cowsay \'hello test infra\'')
    assert c.rc == 0
    assert expected in c.stdout
