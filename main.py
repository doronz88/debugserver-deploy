#!/usr/bin/python3
import os

import click

ENTITLEMENTS = os.path.join(os.path.dirname(__file__), 'debugserver_ent.plist')


@click.command()
@click.argument('debugserver', type=click.Path(exists=True))
@click.argument('output')
def main(debugserver, output):
    """
    Simple utility for patching the original `debugserver` which comes with XCode in include entitlements
    for debugging other processes in a jailbroken device.

    The binary can be obtained from:

    /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/<IOS_VERSION>/DeveloperDiskImage.dmg

    Just replace the <IOS_VERSION> with your correct version.
    """
    if 0 != os.system(f'lipo -thin arm64 {debugserver} -output {output}'):
        print('failed lipo execution. verify its installed and in path')
        return

    if 0 != os.system(f'codesign -s - --entitlements {ENTITLEMENTS} -f --generate-entitlement-der {output}'):
        print('failed codesign execution. verify its installed and in path')
        return

    print('Done. 🍺')


if __name__ == '__main__':
    main()
