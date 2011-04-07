import RepoManager
import argparse

parser = argparse.ArgumentParser(prog="repo-manager", usage="%(prog)s ...")
parser.add_argument("-r", "--default-remote", action='store', required=True)
parser.add_argument("-b", "--default-branch", action='store', required=True)
parser.add_argument("-g", "--github", action='append')
parser.add_argument("-l", "--local-host", action="append", nargs=3)
args = parser.parse_args()

for github_account in args.github:
    RepoManager.GitHubHost(github_account)

for host in args.local_host:
    RepoManager.LocalHost(host[0], host[1], host[2])

RepoManager.Default(args.default_remote, args.default_branch)

print RepoManager.Manifest()
