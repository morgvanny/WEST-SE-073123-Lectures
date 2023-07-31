# Functions

## SWBAT

- Describe what functions are and their central importance in JS
- Review syntax differences between regular functions and arrow functions
- Explain the difference between:
  - Block scope
  - Function scope
  - Global scope
- Understand what it means that a function are first- class -objects
- Explain what a higher-order function is
- Grasp the relationship betweenDescribe what a callback and higher-order functions is

<p align="center">
    <svg host="65bd71144e" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="771px" height="401px" viewBox="-0.5 -0.5 771 401" content="&lt;mxfile&gt;&lt;diagram id=&quot;pAZiludJJASJAjtSt3jZ&quot; name=&quot;Page-1&quot;&gt;7Vrfb9sgEP5rLG0PnWzjX31s03abtEmT+rBnamMHjYCHcZP0rx+OcWwCyRI1idtsLwk+4MJ9d/dx4DhgMlt85rCcfmcZIo7vZgsH3Dm+HyeJ/GwEy1YQuUErKDjOWpHXCx7xC1JCV0lrnKFKGygYIwKXujBllKJUaDLIOZvrw3JG9F8tYYEMwWMKiSn9iTMxbaVJ6PbyLwgX0+6XPVf1zGA3WAmqKczYfCAC9w6YcMZE25otJog02HW4tPMetvSuF8YRFftM8NsJz5DUyja1LrHsjOWsphlqxrsOuJ1PsUCPJUyb3rn0rpRNxYzIJ082lTrEBVpsXZK3NlQGCGIzJPhSDlETAgXNUn+c90DHsZJNByAHHcZQObdYa+7tlw0FgR0OYMDxwDgqVhAcCm3yd2hRJsNKPVJGkQ3LZsxWJNV6K1bzVI1SmSQgL5AaFdvx5ohAgZ917a9BrwvqgckZyjGVqWqz/Bt8krSgmQwJLqhsp9JCxKWgiSQsE+9GdcxwljU6bjmq8At8Wulr4rJkmIrV2sNbJ7yTkpxRoajD83eFpmIJpazPzSHQyc6QvXI/uUGYaHF7pbTvjbLS/qMxZKDG12ewPK+kXze9sl7TXo4KDD99kMZCqQHxj2cgALATTT/WGcDzTQpYy4YUEB2BAa7HydrQzNrgTFnr2UyOiFAppNke/a5Z13FVrZLrRg7w/HLRd8pW0XzDNEWlzEmlTK6j1df2jk0JyWsp4XpnEEtGiKL4qIzQkc2G1vAEBBEaIZHXNBWY0dHZYUxy2Kdc2s0O9k3pULaITbbYVlQdf5M3a6QCUcShuIBtvvXnrn3eC8PoFFkNdKWn2PVjw3GEFTgdPaODaMSU9sya9eDdL7HtfndN5YtbytxvA5QICh3cSnD2C00YYbxnkxwTsiHaP59s3tT9fQSHJro/I9Od0bXFneAY7vRO5M6v9Jml8L87JUWGZ/Snb/qTI1FzupaNzV7RmOwFzJPcWy3UgHdOXMwC1lqbHHyMG1ZhwHLVAuK9YTp6ZQai13Pfv3iQa4PlQk9ywKz6ZLjWs8b6sRliXIo41f2sRhGWk1pgC8FzUYR518Nr+v7PbeDC7mfNQ8nbPKqdNWMDW21/itsX7XWKa8lgMF4GB74BwuVcvwS73wy+7+uXwLw4e+NHmVNmt3zs33K3aPZ/FQD3fwA=&lt;/diagram&gt;&lt;/mxfile&gt;">
    <defs/>
    <g>
        <rect x="0" y="0" width="770" height="400" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <path d="M 350 110 L 413.63 110" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 418.88 110 L 411.88 113.5 L 413.63 110 L 411.88 106.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 110px; margin-left: 384px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                defines
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="384" y="113" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    defines
                </text>
            </switch>
        </g>
        <rect x="230" y="80" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 110px; margin-left: 231px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                (parameter)
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="290" y="114" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    (parameter)
                </text>
            </switch>
        </g>
        <path d="M 150 110 L 223.63 110" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 228.88 110 L 221.88 113.5 L 223.63 110 L 221.88 106.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 107px; margin-left: 187px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 18px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                <font style="font-size: 12px">
                                    accepts
                                </font>
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="187" y="112" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="18px" text-anchor="middle">
                    accepts
                </text>
            </switch>
        </g>
        <rect x="30" y="80" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 110px; margin-left: 31px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                function
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="90" y="114" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    function
                </text>
            </switch>
        </g>
        <path d="M 540 110 L 613.63 110" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 618.88 110 L 611.88 113.5 L 613.63 110 L 611.88 106.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 110px; margin-left: 578px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                generates
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="578" y="113" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    generates
                </text>
            </switch>
        </g>
        <rect x="420" y="80" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 110px; margin-left: 421px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                logic
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="480" y="114" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    logic
                </text>
            </switch>
        </g>
        <rect x="40" y="20" width="690" height="30" fill="none" stroke="none" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 688px; height: 1px; padding-top: 35px; margin-left: 41px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                <font style="font-size: 18px">
                                    Definition
                                </font>
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="385" y="39" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    Definition
                </text>
            </switch>
        </g>
        <rect x="40" y="210" width="690" height="30" fill="none" stroke="none" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 688px; height: 1px; padding-top: 225px; margin-left: 41px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                <font style="font-size: 18px">
                                    Invocation
                                </font>
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="385" y="229" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    Invocation
                </text>
            </switch>
        </g>
        <rect x="620" y="80" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 110px; margin-left: 621px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                return value
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="680" y="114" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    return value
                </text>
            </switch>
        </g>
        <rect x="30" y="270" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 300px; margin-left: 31px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                function
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="90" y="304" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    function
                </text>
            </switch>
        </g>
        <path d="M 150 300 L 223.63 300" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 228.88 300 L 221.88 303.5 L 223.63 300 L 221.88 296.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 297px; margin-left: 187px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 18px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                <font style="font-size: 12px">
                                    accepts
                                </font>
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="187" y="302" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="18px" text-anchor="middle">
                    accepts
                </text>
            </switch>
        </g>
        <rect x="230" y="270" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 300px; margin-left: 231px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                argument
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="290" y="304" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    argument
                </text>
            </switch>
        </g>
        <path d="M 350 300 L 413.63 300" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 418.88 300 L 411.88 303.5 L 413.63 300 L 411.88 296.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 300px; margin-left: 384px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                runs
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="384" y="303" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    runs
                </text>
            </switch>
        </g>
        <rect x="420" y="270" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 300px; margin-left: 421px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                logic
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="480" y="304" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    logic
                </text>
            </switch>
        </g>
        <path d="M 540 300 L 613.63 300" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 618.88 300 L 611.88 303.5 L 613.63 300 L 611.88 296.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 300px; margin-left: 578px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">
                                generates
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="578" y="303" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    generates
                </text>
            </switch>
        </g>
        <rect x="620" y="270" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/>
        <g transform="translate(-0.5 -0.5)">
            <switch>
                <foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;">
                    <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 300px; margin-left: 621px;">
                        <div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;">
                            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">
                                return value
                            </div>
                        </div>
                    </div>
                </foreignObject>
                <text x="680" y="304" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">
                    return value
                </text>
            </switch>
        </g>
    </g>
    <switch>
        <g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/>
        <a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank">
            <text text-anchor="middle" font-size="10px" x="50%" y="100%">
                Viewer does not support full SVG 1.1
            </text>
        </a>
    </switch>
</svg>
</p>

## Deliverables

Easley's Technical Books has asked us to build them an inventory management tool for their employees.

Today we will work on functions that may help us accomplish some tasks related to displaying data on the application.

The variable inventory is an array of book objects in index.js. Inventory[0] is the following book.

```
        {
            id:1,
            title: 'Eloquent JavaScript: A Modern Introduction to Programming',
            author: 'Marjin Haverbeke',
            price: 10.00,
            reviews: [{userID: 1, content:'Good book, but not great for new coders'}],
            inventory: 10,
            imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg',

        }
```

- Demo Function Decoration:
  - Declare a function that takes a book as a parameter and returns the book's price formatted to look like currency. Given inventory[0] the return should be '$10.00"
- Demo Function Expressions:
  - Create a function Expression that takes a book as a parameter and returns a string consisting of the title and author of the book. Given inventory[0] the return should be 'Title: Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke'
- Demo arrow functions pt1:
  - Create an arrow function that takes a book as a parameter and returns a string noting a book is on sale. Given inventory[0] the return should be 'Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke is on sale!'
- Demo arrow functions pt2:
  - Create an arrow function that takes a discount and a book as parameters. Return the book price divided by the discount. Given inventory[0] and 2 the return should be 5.00
- Demo Scope:

  - Create a variable in the global scope and set it to a book's title.
  - Create a function that takes title, price, author, and imageUrl as parameters.
  - Create a variable in function scope and set it to an empty object.
  - Assign the object the properties of title, price, and author with their values set to their corresponding parameters. Add a key of inventory and set it to 0, and a key of reviews set to an empty array.
  - Create a conditional statement that checks whether the imageUrl has a value. If it has a value, give the object the property of imageUrl with its value set to the parameter. Else create a variable with the value of 'placeHolderImage.jpg' within block scope and give the object property of imageUrl set to the variable in block scope. (Note: we can give the parameter a default value here, but this section's purpose is to demo scope.)

  - Return book object
  - Invoke the function with arguments and pass it to inventory.push so the return value is added to the inventory array.
  - Show the different levels of scope using console.logs or debuggers. Where do we have access to variables declared in global scope? Where do we have access to variables declared in function scope? Where do we have access to variables declared at the block level? What does local scope mean?

- Demo Callbacks
  - Create a function that takes a callback function and an array
  - Inside the function create a variable and set it to an empty array.
  - Loop through the array property. Within the block, invoke the callback function and pass it to the array element as an argument.
  - The return value of the callback should be pushed to the new array variable.
  - Return the new array variable.
  - Test the function by passing the inventory array and one of our previous functions as its callback. (The function must take a single book as a parameter)
- Bonus
  - Demo .map as a practical example of callbacks.

## Functions

Functions are like a little program. They consist of a set of statements/tasks and return a value or undefined.

```
// This is a function delcoration
// This function is returning the string of 'hi'
function sayHi() {
    return 'hi'
}
//This is a function reference but it doesn't actually run the function.
sayhi

// To run or call or invoke (all the same thing). Write the functions name and add a pair of ()
sayHi()

// This functions console.logs the string of 'hello' but returns undefined because it does not have the return keyword.

function sayHello(){
    console.log('hello')
}

sayHello()

// logging and returning are not the same thing. A return value becomes the value of an invoked function, while a console.log only logs something to the console.

```

Functions can take unique localized variables called parameters. When the function is invoked, it's passed an argument that becomes the parameter's value.

```

function squareNumb(num){
    //num is the parameter, it is scoped to the inside of the function
    return num*num
}
// 2 is the argument. The value of num in the above function becomes 2.
squareNumb(2)


// functions can take multiple parameters.
function addTwo(num1, numb2){
    return num1 + num2
}
addTwo(5,10)

```

Arrow functions are another way to declare functions with some added benefits.

```
// An arrow function can avoid {} if it's return done on a single line or with ()
// An arrow function with a single paramater doesn't need the () around the paramater.
const faveFood = food =>  `My fave food is ${food}`
const faveFood = food => (
     `My fave food is ${food}`
)
faveFood('cookies')

```

Arrow functions also have the added benefit of passing context, but we won't be covering that today.

## Callbacks and HigherOrder Functions

Functions in JavaScript are treated like any other variable. When functions are treated like this, we refer to them as First class. One of the most significant benefits of this is that functions in JavaScript can be passed as arguments to other functions.

```
// A function that returns a function is called a Higher-Order Function.

const outsideFunction = () => {
    return () => {
        //inside function
    }
}

//A function that is taken as an argument is a callback

const opening => (openingVideo, credits){
    return openingVideo(credits)
}

const taskingHistory(){
    //... video functionality here
}

const crashCourse(){
    //... video functionality here
}

opening(crashCourse, 'Hank Green')

```
