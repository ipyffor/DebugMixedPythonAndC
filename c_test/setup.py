# setup.py

from distutils.core import setup, Extension

def main():
    setup(
          name="fputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="hanbing",
          author_email="beatmight@gmail.com",
          ext_modules=[Extension(
                "fputs", ["fputsmodule.c"], 
                language="c++",
                # Linux下注释这两个参数
            #     extra_compile_args=['/Zi'],
            #     extra_link_args=['/DEBUG']
            )],
      )

if __name__ == "__main__":
    main()