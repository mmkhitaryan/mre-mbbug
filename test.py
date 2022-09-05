import r2pipe

r = r2pipe.open()

FILE_NAME = "README"

r.cmd('ood')
r.cmd('aaa')

all_imports = r.cmdj('iaj')

for r2_import in all_imports["imports"]:
    if r2_import["name"]=="opendir":
        opendir_pointer = r2_import["plt"]

last_pointer = ''

r.cmd(f'dcu {opendir_pointer}')

# there is no way to stop loop
done = False
while not done:
    poiner_from_stack = str(r.cmdj('pxqj 8 @rsp')[0])

    # skip same pointer
    if last_pointer != poiner_from_stack:
        heap_read = r.cmd(f'prx 1024 @ {poiner_from_stack}')
        if FILE_NAME in heap_read:
            print(heap_read)
            done = True
        last_pointer = poiner_from_stack

    r.cmd('ds')
