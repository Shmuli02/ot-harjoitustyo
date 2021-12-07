from invoke import task

@task
def commandline(ctx):
    ctx.run("python3 src/index.py commandline")

@task
def start(ctx):
    ctx.run("python3 src/index.py graphic")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task()
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage html")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def build(ctx):
    ctx.run('python3 src/build.py')