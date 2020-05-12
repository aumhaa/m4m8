{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 0,
			"revision" : 6,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 242.0, 234.0, 502.0, 557.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 9.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 20.0, 20.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "This will zero out the all patterns on the currently selected presets.",
					"id" : "obj-81",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1275.799999999999727, 497.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 199.0, 205.0, 189.0, 22.0 ],
					"text" : "Initialize All Presets",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings20"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-79",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 231.5, 551.0, 66.0, 19.0 ],
					"text" : "prepend send"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-77",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 177.0, 551.0, 48.0, 19.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-80",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 303.0, 670.5, 31.0, 19.0 ],
					"text" : "defer",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-78",
					"index" : 0,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 426.0, 683.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 16.0,
					"id" : "obj-76",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1134.199951000000056, 203.0, 127.300049000000001, 42.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 404.25, 266.5, 78.5, 42.0 ],
					"text" : "BEHAVE\nENABLE",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-74",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1165.5, 466.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 518.0, 73.0, 18.0 ],
					"text" : "Part 16",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-75",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 466.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 503.0, 73.0, 18.0 ],
					"text" : "Part 15",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-67",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 454.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 491.0, 73.0, 18.0 ],
					"text" : "Part 14",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-68",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 438.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 477.0, 73.0, 18.0 ],
					"text" : "Part 13",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-69",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 423.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 464.0, 73.0, 30.0 ],
					"text" : "Part 12\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-70",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 407.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 449.0, 73.0, 18.0 ],
					"text" : "Part 11",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-71",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 391.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 434.0, 73.0, 30.0 ],
					"text" : "Part 10\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-72",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 375.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 421.0, 73.0, 30.0 ],
					"text" : "Part 9\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-73",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 359.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 407.0, 73.0, 18.0 ],
					"text" : "Part 8",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-40",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 341.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 393.0, 73.0, 18.0 ],
					"text" : "Part 7",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-41",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 325.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 379.0, 73.0, 18.0 ],
					"text" : "Part 6",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-60",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 310.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 365.0, 73.0, 30.0 ],
					"text" : "Part 5\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-61",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 294.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 351.0, 73.0, 30.0 ],
					"text" : "Part 4\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-62",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 278.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 336.0, 73.0, 30.0 ],
					"text" : "Part 3\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-63",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 262.0, 96.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 321.0, 73.0, 30.0 ],
					"text" : "Part 2\n",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-64",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1160.5, 246.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 307.0, 73.0, 18.0 ],
					"text" : "Part 1",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"activecolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"disabled" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
					"id" : "obj-65",
					"itemtype" : 1,
					"maxclass" : "radiogroup",
					"numinlets" : 1,
					"numoutlets" : 1,
					"offset" : 14,
					"outlettype" : [ "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 1142.5, 246.0, 18.0, 226.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 399.0, 307.0, 18.0, 226.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 3,
							"parameter_longname" : "behavior_enables",
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_mmax" : 15.0,
							"parameter_initial" : [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
							"parameter_shortname" : "behavior_enables"
						}

					}
,
					"size" : 16,
					"values" : [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
					"varname" : "behavior_enables"
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-66",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1134.199951000000056, 203.0, 136.0, 280.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 395.0, 263.5, 98.0, 285.5 ],
					"proportion" : 0.39
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-53",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 490.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 238.0, 73.0, 18.0 ],
					"text" : "Play",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-54",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 474.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 222.0, 73.0, 18.0 ],
					"text" : "Freewheel",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-55",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 459.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 207.0, 73.0, 18.0 ],
					"text" : "Global Preset",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-56",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 443.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 191.0, 73.0, 18.0 ],
					"text" : "Single Preset",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-57",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 427.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 175.0, 73.0, 18.0 ],
					"text" : "Mute",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-58",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 411.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 159.0, 73.0, 18.0 ],
					"text" : "Add",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-59",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1027.199951000000056, 395.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 143.0, 73.0, 18.0 ],
					"text" : "Select",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-52",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 901.0, 516.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 117.0, 73.0, 18.0 ],
					"text" : "Accent",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-51",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 901.0, 497.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 101.0, 73.0, 18.0 ],
					"text" : "Poly Play",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-50",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 901.0, 482.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 85.0, 73.0, 18.0 ],
					"text" : "Poly Record",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-49",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 901.0, 459.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 70.0, 73.0, 18.0 ],
					"text" : "Global Preset",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-48",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 902.0, 436.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 54.0, 73.0, 18.0 ],
					"text" : "Single Preset",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-47",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 902.0, 412.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 38.0, 73.0, 18.0 ],
					"text" : "Behaviour",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-46",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 904.0, 395.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 22.0, 73.0, 18.0 ],
					"text" : "Length",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-44",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 903.0, 375.0, 96.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 417.0, 6.0, 73.0, 18.0 ],
					"text" : "Mute",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"activecolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"disabled" : [ 0, 0, 0, 0, 0, 0, 0 ],
					"id" : "obj-38",
					"itemtype" : 1,
					"maxclass" : "radiogroup",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 1009.200012000000015, 394.0, 18.0, 114.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 399.0, 143.0, 18.0, 114.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 3,
							"parameter_longname" : "padmodesenabled",
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_mmax" : 6.0,
							"parameter_initial" : [ 1, 1, 1, 1, 1, 1, 1, 1 ],
							"parameter_shortname" : "padmodesenabled"
						}

					}
,
					"size" : 7,
					"values" : [ 1, 1, 1, 1, 1, 1, 1 ],
					"varname" : "padmodesenabled"
				}

			}
, 			{
				"box" : 				{
					"activecolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"disabled" : [ 0, 0, 0, 0, 0, 0, 0, 0 ],
					"id" : "obj-37",
					"itemtype" : 1,
					"maxclass" : "radiogroup",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 875.90002400000003, 386.0, 18.0, 130.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 399.0, 5.0, 18.0, 130.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 3,
							"parameter_longname" : "keymodesenabled",
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_mmax" : 7.0,
							"parameter_initial" : [ 1, 1, 1, 1, 1, 1, 1, 1 ],
							"parameter_shortname" : "keymodesenabled"
						}

					}
,
					"size" : 8,
					"values" : [ 1, 1, 1, 1, 1, 1, 1, 1 ],
					"varname" : "radiogroup"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 319.0, 479.0, 111.0, 19.0 ],
					"text" : "prepend behavegraph_in",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-111",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 285.5, 538.5, 104.5, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 122.0, 104.0, 109.0, 20.0 ],
					"text" : "Poly Output Port",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-103",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 303.0, 645.0, 71.0, 19.0 ],
					"text" : "prepend output",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"allowdrag" : 0,
					"arrow" : 0,
					"bgcolor" : [ 0.847058823529412, 0.847058823529412, 0.847058823529412, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.847058823529412, 0.847058823529412, 0.847058823529412, 1.0 ],
					"bgfillcolor_color1" : [ 0.376471, 0.384314, 0.4, 1.0 ],
					"bgfillcolor_color2" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
					"bgfillcolor_proportion" : 0.39,
					"bgfillcolor_type" : "color",
					"fontsize" : 10.0,
					"id" : "obj-105",
					"items" : [ "IAC Bus Bus 1", ",", "IAC Bus Drumchooser", ",", "Sensel Morph", ",", "Daemon Output 0", ",", "Daemon Output 1", ",", "Daemon Output 2", ",", "Daemon Output 3", ",", "Daemon Output 4", ",", "Daemon Output 5", ",", "Daemon Output 6", ",", "Daemon Output 7", ",", "to Max 1", ",", "to Max 2", ",", "<none>" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 262.5, 614.5, 100.0, 20.0 ],
					"pattrmode" : 1,
					"presentation" : 1,
					"presentation_rect" : [ 236.0, 104.0, 119.0, 20.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 3,
							"parameter_longname" : "lh_output_port",
							"parameter_invisible" : 1,
							"parameter_mmax" : 6.0,
							"parameter_shortname" : "lh_output_port"
						}

					}
,
					"textcolor" : [ 0.15, 0.15, 0.15, 1.0 ],
					"varname" : "lh_output_port"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Helvetica",
					"fontsize" : 10.0,
					"id" : "obj-102",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 231.5, 583.5, 50.5, 18.0 ],
					"text" : "midi4l",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-21",
					"index" : 0,
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 231.5, 512.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-110",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 46.0, 631.0, 55.0, 19.0 ],
					"save" : [ "#N", "thispatcher", ";", "#Q", "end", ";" ],
					"text" : "thispatcher",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-108",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 476.0, 555.0, 89.0, 19.0 ],
					"text" : "prepend settingsgui",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-109",
					"maxclass" : "newobj",
					"numinlets" : 7,
					"numoutlets" : 1,
					"outlettype" : [ "list" ],
					"patching_rect" : [ 476.0, 530.0, 818.799999999999727, 19.0 ],
					"text" : "funnel 7 11",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 0.996078431372549, 0.666666666666667, 0.666666666666667, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create rulebends for all currently selected presets.",
					"id" : "obj-107",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 609.299987999999985, 490.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 36.0, 150.0, 51.0, 13.0 ],
					"text" : "Global",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"texton" : "Global",
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings10[2]"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create rulebends for all currently selected presets.",
					"id" : "obj-106",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 476.0, 490.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 303.0, 150.0, 51.0, 13.0 ],
					"text" : "All",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"texton" : "All",
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings10[1]"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomize the rules used by all the behavior patterns.",
					"id" : "obj-16",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 742.59997599999997, 490.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 300.0, 243.0, 67.0, 18.0 ],
					"text" : "Randomize",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings12"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "Each rule can be applied to any step of a behavior sequence to the left.",
					"id" : "obj-101",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 365.0, 187.0, 42.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 312.0, 271.0, 42.0, 20.0 ],
					"text" : "Rules",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create behaviors for all currently selected presets.",
					"id" : "obj-33",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 717.0, 305.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 232.0, 170.0, 61.0, 20.0 ],
					"text" : "Behaviors",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings9"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-99",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 471.0, 379.0, 89.0, 19.0 ],
					"text" : "prepend settingsgui",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-100",
					"maxclass" : "newobj",
					"numinlets" : 6,
					"numoutlets" : 1,
					"outlettype" : [ "list" ],
					"patching_rect" : [ 471.0, 335.0, 429.5, 19.0 ],
					"text" : "funnel 6 5",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "This will zero out the all patterns on the currently selected presets.",
					"id" : "obj-98",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 882.0, 303.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 8.0, 205.0, 189.0, 22.0 ],
					"text" : "Initialize Preset",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings11"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create rulebends for all currently selected presets.",
					"id" : "obj-96",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 799.0, 304.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 299.0, 170.0, 61.0, 20.0 ],
					"text" : "Rulebends",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings10"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create durations for all currently selected presets.",
					"id" : "obj-95",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 635.0, 305.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 165.0, 170.0, 61.0, 20.0 ],
					"text" : "Durations",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings8"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create velocities for all currently selected presets.",
					"id" : "obj-94",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 553.0, 305.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 98.0, 170.0, 61.0, 20.0 ],
					"text" : "Velocities",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings7"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Randomly create steps for all currently selected presets.",
					"id" : "obj-93",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 471.0, 305.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 31.0, 170.0, 61.0, 20.0 ],
					"text" : "Patterns",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1,
					"varname" : "settings6"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 16.0,
					"id" : "obj-31",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 635.0, 275.0, 102.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 143.0, 145.0, 102.0, 24.0 ],
					"text" : "Randomize",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-24",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 461.0, 299.0, 491.0, 66.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 8.0, 143.0, 380.0, 55.0 ],
					"proportion" : 0.39
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.674509803921569, 0.674509803921569, 0.674509803921569, 1.0 ],
					"activeslidercolor" : [ 0.94902, 0.756863, 0.309804, 1.0 ],
					"activetricolor" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"bordercolor" : [ 0.27451, 0.32549, 0.4, 1.0 ],
					"fontsize" : 11.0,
					"hint" : "This is the amount of steps transposed when pressing the step transpose encoder buttons.",
					"id" : "obj-5",
					"maxclass" : "live.numbox",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 895.0, 203.0, 38.0, 17.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 236.0, 81.0, 119.0, 17.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 1,
							"parameter_unitstyle" : 7,
							"parameter_linknames" : 1,
							"parameter_mmin" : 1.0,
							"parameter_longname" : "setting4[1]",
							"parameter_invisible" : 1,
							"parameter_mmax" : 96.0,
							"parameter_order" : 1006,
							"parameter_shortname" : "transposesteps"
						}

					}
,
					"tricolor" : [ 0.815686, 0.847059, 0.886275, 1.0 ],
					"tricolor2" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"varname" : "setting4[1]"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-23",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 760.0, 146.0, 66.0, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 132.0, 79.0, 99.0, 20.0 ],
					"text" : "Tranpose Steps",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.8, 0.8, 0.8, 1.0 ],
					"bgoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"fontface" : 1,
					"fontsize" : 10.0,
					"hint" : "Select a DrumRack in Live, then press this button.  Hex will lock it's device controls to that DrumRack.",
					"id" : "obj-18",
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 743.0, 200.0, 100.0, 20.0 ],
					"text" : "Capture Currently Selected Instrument",
					"textcolor" : [ 0.007843, 0.007843, 0.007843, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.1, 0.1, 0.1, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-97",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 0,
							"revision" : 6,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 25.0, 69.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 9.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-95",
									"maxclass" : "button",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 113.0, 100.0, 20.0, 20.0 ]
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-94",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 154.0, 204.0, 32.5, 17.0 ],
									"text" : "% 8"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-93",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 94.0, 268.0, 52.0, 17.0 ],
									"text" : "pack 0 0 0"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-24",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 155.0, 228.0, 32.5, 17.0 ],
									"text" : "+ 1"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-23",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 98.0, 207.0, 32.5, 17.0 ],
									"text" : "/ 8"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-18",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 50.0, 207.0, 32.5, 17.0 ],
									"text" : "% 8"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 9.0,
									"id" : "obj-5",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 3,
									"outlettype" : [ "bang", "bang", "int" ],
									"patching_rect" : [ 68.0, 125.0, 46.0, 17.0 ],
									"text" : "uzi 56"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-96",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 94.0, 345.0, 25.0, 25.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-93", 0 ],
									"source" : [ "obj-18", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-93", 1 ],
									"source" : [ "obj-23", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-93", 2 ],
									"source" : [ "obj-24", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-18", 0 ],
									"order" : 2,
									"source" : [ "obj-5", 2 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-23", 0 ],
									"order" : 1,
									"source" : [ "obj-5", 2 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-94", 0 ],
									"order" : 0,
									"source" : [ "obj-5", 2 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-96", 0 ],
									"source" : [ "obj-93", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-24", 0 ],
									"source" : [ "obj-94", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"source" : [ "obj-95", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 219.0, 479.0, 62.0, 19.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"fontsize" : 9.0,
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p init_ruledef",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-91",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 426.0, 658.5, 31.0, 19.0 ],
					"text" : "defer",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-90",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 496.0, 246.0, 89.0, 19.0 ],
					"text" : "prepend settingsgui",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-88",
					"maxclass" : "newobj",
					"numinlets" : 5,
					"numoutlets" : 1,
					"outlettype" : [ "list" ],
					"patching_rect" : [ 496.0, 226.0, 418.0, 19.0 ],
					"text" : "funnel 5",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 96.0, 490.0, 32.5, 19.0 ],
					"text" : "+ 1",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 134.0, 490.0, 32.5, 19.0 ],
					"text" : "+ 1",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 96.0, 512.0, 95.0, 19.0 ],
					"text" : "sprintf nsub %i %i %i",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-27",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "int", "int" ],
					"patching_rect" : [ 96.0, 466.0, 95.0, 19.0 ],
					"text" : "unpack 0 0 0",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"coll_data" : 					{
						"count" : 8,
						"data" : [ 							{
								"key" : 0,
								"value" : [ 1, 1, 1, 1, 1, 1, 1, 1 ]
							}
, 							{
								"key" : 1,
								"value" : [ 1, 1, 1, 1, 1, 1, 1, 1 ]
							}
, 							{
								"key" : 2,
								"value" : [ 2, 2, 2, 2, 2, 2, 2, 2 ]
							}
, 							{
								"key" : 3,
								"value" : [ 3, 3, 3, 3, 3, 3, 3, 3 ]
							}
, 							{
								"key" : 4,
								"value" : [ 4, 4, 4, 4, 4, 4, 4, 4 ]
							}
, 							{
								"key" : 5,
								"value" : [ 5, 5, 5, 5, 5, 5, 5, 5 ]
							}
, 							{
								"key" : 6,
								"value" : [ 6, 6, 6, 6, 6, 6, 6, 6 ]
							}
, 							{
								"key" : 7,
								"value" : [ 7, 7, 7, 7, 7, 7, 7, 7 ]
							}
 ]
					}
,
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 96.0, 532.0, 59.5, 19.0 ],
					"saved_object_attributes" : 					{
						"embed" : 1
					}
,
					"text" : "coll ---rules",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"color" : [ 0.8, 0.84, 0.71, 1.0 ],
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 9.0,
					"frozen_object_attributes" : 					{
						"invisible" : 1
					}
,
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 58.0, 157.0, 63.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 39.0, 143.0, 63.0, 19.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_initial" : [ 0, 0, 1, 0, 1, 1, 0, 2, 1, 0, 3, 1, 0, 4, 1, 0, 5, 1, 0, 6, 1, 0, 7, 1, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 3, 2, 1, 4, 2, 1, 5, 2, 1, 6, 2, 1, 7, 2, 2, 0, 3, 2, 1, 3, 2, 2, 3, 2, 3, 3, 2, 4, 3, 2, 5, 3, 2, 6, 3, 2, 7, 3, 3, 0, 4, 3, 1, 4, 3, 2, 4, 3, 3, 4, 3, 4, 4, 3, 5, 4, 3, 6, 4, 3, 7, 4, 4, 0, 5, 4, 1, 5, 4, 2, 5, 4, 3, 5, 4, 4, 5, 4, 5, 5, 4, 6, 5, 4, 7, 5, 5, 0, 6, 5, 1, 6, 5, 2, 6, 5, 3, 6, 5, 4, 6, 5, 5, 6, 5, 6, 6, 5, 7, 6, 6, 0, 7, 6, 1, 7, 6, 2, 7, 6, 3, 7, 6, 4, 7, 6, 5, 7, 6, 6, 7, 6, 7, 7 ],
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_linknames" : 1,
							"parameter_longname" : "ruledefs",
							"parameter_order" : 1020,
							"parameter_shortname" : "ruledefs",
							"parameter_type" : 3
						}

					}
,
					"saved_object_attributes" : 					{
						"initial" : [ 0, 0, 1, 0, 1, 1, 0, 2, 1, 0, 3, 1, 0, 4, 1, 0, 5, 1, 0, 6, 1, 0, 7, 1, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 3, 2, 1, 4, 2, 1, 5, 2, 1, 6, 2, 1, 7, 2, 2, 0, 3, 2, 1, 3, 2, 2, 3, 2, 3, 3, 2, 4, 3, 2, 5, 3, 2, 6, 3, 2, 7, 3, 3, 0, 4, 3, 1, 4, 3, 2, 4, 3, 3, 4, 3, 4, 4, 3, 5, 4, 3, 6, 4, 3, 7, 4, 4, 0, 5, 4, 1, 5, 4, 2, 5, 4, 3, 5, 4, 4, 5, 4, 5, 5, 4, 6, 5, 4, 7, 5, 5, 0, 6, 5, 1, 6, 5, 2, 6, 5, 3, 6, 5, 4, 6, 5, 5, 6, 5, 6, 6, 5, 7, 6, 6, 0, 7, 6, 1, 7, 6, 2, 7, 6, 3, 7, 6, 4, 7, 6, 5, 7, 6, 6, 7, 6, 7, 7 ],
						"parameter_enable" : 1,
						"parameter_mappable" : 0
					}
,
					"text" : "pattr ruledefs",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"varname" : "ruledefs"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.674509803921569, 0.674509803921569, 0.674509803921569, 1.0 ],
					"activeslidercolor" : [ 0.94902, 0.756863, 0.309804, 1.0 ],
					"activetricolor" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"bordercolor" : [ 0.27451, 0.32549, 0.4, 1.0 ],
					"fontsize" : 11.0,
					"hint" : "This box should correspond to the assigned not of the first instrument in the DrumRack you are controlling.",
					"id" : "obj-36",
					"maxclass" : "live.numbox",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 696.0, 206.0, 38.0, 17.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 236.0, 59.0, 119.0, 17.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_type" : 1,
							"parameter_unitstyle" : 8,
							"parameter_linknames" : 1,
							"parameter_longname" : "setting3[1]",
							"parameter_invisible" : 1,
							"parameter_mmax" : 96.0,
							"parameter_order" : 1007,
							"parameter_shortname" : "live.numbox"
						}

					}
,
					"tricolor" : [ 0.815686, 0.847059, 0.886275, 1.0 ],
					"tricolor2" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"varname" : "setting3[1]"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-35",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 696.0, 146.0, 52.0, 47.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 107.0, 57.0, 123.0, 20.0 ],
					"text" : "Global Chain Offset",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.674509803921569, 0.674509803921569, 0.674509803921569, 1.0 ],
					"bordercolor" : [ 0.27451, 0.32549, 0.4, 1.0 ],
					"hint" : "This determines whether a timing change happens instantaneously or not.",
					"hltcolor" : [ 0.976471, 0.823529, 0.054902, 1.0 ],
					"id" : "obj-29",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 596.0, 206.0, 81.0, 15.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 236.0, 37.0, 118.0, 15.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_defer" : 1,
							"parameter_type" : 2,
							"parameter_unitstyle" : 0,
							"parameter_linknames" : 1,
							"parameter_longname" : "setting2[1]",
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_mmax" : 1,
							"parameter_initial" : [ 0 ],
							"parameter_order" : 1005,
							"parameter_shortname" : "keymode",
							"parameter_enum" : [ "at beginning of bar", "immediately" ]
						}

					}
,
					"tricolor" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"varname" : "setting2[1]"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-26",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 596.0, 146.0, 81.0, 47.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 81.0, 35.0, 148.0, 20.0 ],
					"text" : "Timing changes happen",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-25",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 476.0, 146.0, 108.0, 47.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 28.0, 13.0, 202.0, 20.0 ],
					"text" : "Select + Hold temporarily reveals",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.674509803921569, 0.674509803921569, 0.674509803921569, 1.0 ],
					"bordercolor" : [ 0.27451, 0.32549, 0.4, 1.0 ],
					"hint" : "This setting determines what happens when holding down a sequence select button for a moment.",
					"hltcolor" : [ 0.976471, 0.823529, 0.054902, 1.0 ],
					"id" : "obj-45",
					"maxclass" : "live.menu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 496.0, 206.0, 88.0, 15.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 236.0, 16.0, 118.0, 15.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_defer" : 1,
							"parameter_type" : 2,
							"parameter_unitstyle" : 0,
							"parameter_linknames" : 1,
							"parameter_longname" : "setting1[1]",
							"parameter_initial_enable" : 1,
							"parameter_invisible" : 1,
							"parameter_mmax" : 6,
							"parameter_initial" : [ 3 ],
							"parameter_order" : 1004,
							"parameter_shortname" : "keymode",
							"parameter_enum" : [ "mute", "length", "behavior", "single preset", "global preset", "polyrec", "polyplay" ]
						}

					}
,
					"tricolor" : [ 0.572549, 0.615686, 0.658824, 1.0 ],
					"varname" : "setting1[1]"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 16.0,
					"hint" : "Create a sequence of rules for each behavior type. ",
					"id" : "obj-22",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 164.0, 118.0, 102.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 122.0, 239.0, 102.0, 24.0 ],
					"text" : "BEHAVIORS",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-20",
					"linecount" : 15,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 60.0, 213.0, 27.0, 224.0 ],
					"presentation" : 1,
					"presentation_linecount" : 15,
					"presentation_rect" : [ 32.0, 299.0, 27.0, 224.0 ],
					"text" : "1  \n\n2  \n\n3  \n\n4 \n\n5 \n\n6  \n\n7 \n\n8 ",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-17",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 51.0, 186.0, 42.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 23.0, 272.0, 42.0, 20.0 ],
					"text" : "Bar #",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "The selected step will trigger an action in Plinko, if present in the same project.",
					"id" : "obj-15",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 349.0, 424.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 321.0, 510.0, 66.0, 20.0 ],
					"text" : "Plink",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "The selected step will be triggered and repeated, its tempo and repetitions determined by rulebend.",
					"id" : "obj-14",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 350.0, 394.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 322.0, 480.0, 66.0, 20.0 ],
					"text" : "Repeat",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "The selected step will be triggered with a delay corresponding to the rulebend amount.",
					"id" : "obj-13",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 350.0, 364.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 322.0, 450.0, 66.0, 20.0 ],
					"text" : "Delay",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "The selected step will be triggered, and block any other steps that aren't also set to dominate.  The length of domination is determined by rulebend.",
					"id" : "obj-12",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 349.0, 334.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 321.0, 420.0, 66.0, 20.0 ],
					"text" : "Dominate",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "The selected step will be triggered if other steps with the same rulebend are triggered on the same step.",
					"id" : "obj-11",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 349.0, 305.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 321.0, 391.0, 66.0, 20.0 ],
					"text" : "Sympathy",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "Selected step will randomly play, based on the weighting supplied by its corresponding rulebend",
					"id" : "obj-10",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 350.0, 275.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 322.0, 361.0, 66.0, 20.0 ],
					"text" : "Random",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "Selected step will be played",
					"id" : "obj-9",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 350.0, 245.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 322.0, 331.0, 66.0, 20.0 ],
					"text" : "Trigger ",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"hint" : "Selected step will be ignored",
					"id" : "obj-8",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 350.0, 215.0, 66.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 322.0, 301.0, 66.0, 20.0 ],
					"text" : "No action",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "fpic",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "jit_matrix" ],
					"patching_rect" : [ 319.0, 209.0, 29.0, 240.0 ],
					"pic" : "rgb_horizontal.png",
					"presentation" : 1,
					"presentation_rect" : [ 291.0, 295.0, 30.0, 240.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "fpic",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "jit_matrix" ],
					"patching_rect" : [ 97.0, 180.0, 211.0, 30.0 ],
					"pic" : "RGB_button_abc.png",
					"presentation" : 1,
					"presentation_rect" : [ 69.0, 266.0, 211.0, 30.0 ],
					"xoffset" : -270.0
				}

			}
, 			{
				"box" : 				{
					"autosize" : 1,
					"cellpict" : "rgb_only.png",
					"clickedimage" : 0,
					"columns" : 7,
					"hint" : "Click on each square to change its rule assignment.",
					"horizontalmargin" : 0,
					"id" : "obj-4",
					"inactiveimage" : 0,
					"invisiblebkgnd" : 1,
					"maxclass" : "matrixctrl",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "list", "list" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 96.0, 214.0, 210.0, 240.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 69.0, 295.0, 210.0, 240.0 ],
					"range" : 8,
					"rows" : 8,
					"varname" : "rulemap",
					"verticalmargin" : 0
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-2",
					"index" : 0,
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 46.0, 594.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-19",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 35.0, 148.0, 382.0, 315.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 7.0, 234.0, 382.0, 315.0 ],
					"proportion" : 0.39
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-86",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 471.0, 135.0, 382.0, 92.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 8.0, 5.0, 380.0, 130.0 ],
					"proportion" : 0.39
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-42",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 901.0, 375.0, 98.0, 146.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 395.0, 5.0, 98.0, 130.0 ],
					"proportion" : 0.39
				}

			}
, 			{
				"box" : 				{
					"angle" : 0.0,
					"bgcolor" : [ 0.462745098039216, 0.462745098039216, 0.462745098039216, 1.0 ],
					"border" : 1,
					"bordercolor" : [ 0.325490196078431, 0.325490196078431, 0.325490196078431, 1.0 ],
					"id" : "obj-43",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1009.200012000000015, 375.0, 115.0, 142.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 395.0, 143.0, 98.0, 114.0 ],
					"proportion" : 0.39
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-4", 0 ],
					"midpoints" : [ 89.5, 179.5, 105.5, 179.5 ],
					"source" : [ "obj-1", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-99", 0 ],
					"source" : [ "obj-100", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-105", 0 ],
					"midpoints" : [ 272.5, 605.5, 272.0, 605.5 ],
					"source" : [ "obj-102", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-80", 0 ],
					"source" : [ "obj-103", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-103", 0 ],
					"source" : [ "obj-105", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 0 ],
					"source" : [ "obj-106", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 1 ],
					"source" : [ "obj-107", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-91", 0 ],
					"midpoints" : [ 485.5, 583.0, 435.5, 583.0 ],
					"source" : [ "obj-108", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-108", 0 ],
					"source" : [ "obj-109", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 2 ],
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-88", 3 ],
					"midpoints" : [ 752.5, 222.5, 804.75, 222.5 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-110", 0 ],
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-79", 0 ],
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-28", 2 ],
					"source" : [ "obj-27", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-27", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-32", 0 ],
					"source" : [ "obj-27", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-3", 0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-88", 1 ],
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-28", 1 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-28", 0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 3 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-88", 2 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 3 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 4 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-91", 0 ],
					"midpoints" : [ 328.5, 510.0, 435.5, 510.0 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-27", 0 ],
					"order" : 1,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-39", 0 ],
					"midpoints" : [ 105.5, 466.0, 328.5, 466.0 ],
					"order" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-88", 0 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-88", 4 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-109", 5 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 0 ],
					"source" : [ "obj-77", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 0 ],
					"source" : [ "obj-79", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-102", 0 ],
					"midpoints" : [ 312.5, 695.0, 397.0, 695.0, 397.0, 573.5, 241.0, 573.5 ],
					"source" : [ "obj-80", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-109", 6 ],
					"source" : [ "obj-81", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-90", 0 ],
					"source" : [ "obj-88", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-91", 0 ],
					"midpoints" : [ 505.5, 278.0, 435.5, 278.0 ],
					"source" : [ "obj-90", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-78", 0 ],
					"source" : [ "obj-91", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 0 ],
					"source" : [ "obj-93", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 1 ],
					"source" : [ "obj-94", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 2 ],
					"source" : [ "obj-95", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 4 ],
					"source" : [ "obj-96", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-100", 5 ],
					"source" : [ "obj-98", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.8, 0.8, 0.8, 0.9 ],
					"destination" : [ "obj-91", 0 ],
					"midpoints" : [ 480.5, 429.5, 435.5, 429.5 ],
					"source" : [ "obj-99", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-36" : [ "setting3[1]", "live.numbox", 1007 ],
			"obj-1" : [ "ruledefs", "ruledefs", 1020 ],
			"obj-37" : [ "keymodesenabled", "keymodesenabled", 0 ],
			"obj-65" : [ "behavior_enables", "behavior_enables", 0 ],
			"obj-29" : [ "setting2[1]", "keymode", 1005 ],
			"obj-105" : [ "lh_output_port", "lh_output_port", 0 ],
			"obj-45" : [ "setting1[1]", "keymode", 1004 ],
			"obj-38" : [ "padmodesenabled", "padmodesenabled", 0 ],
			"obj-5" : [ "setting4[1]", "transposesteps", 1006 ],
			"parameterbanks" : 			{

			}

		}
,
		"dependency_cache" : [ 			{
				"name" : "rgb_only.png",
				"bootpath" : "~/Documents/Max 8/Packages/mod/javascript/accent",
				"patcherrelativepath" : "../accent",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "RGB_button_abc.png",
				"bootpath" : "~/Documents/Max 8/Packages/mod/javascript/hex",
				"patcherrelativepath" : ".",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "rgb_horizontal.png",
				"bootpath" : "~/Documents/Max 8/Packages/mod/javascript/accent",
				"patcherrelativepath" : "../accent",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "midi4l.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0,
		"bgcolor" : [ 0.2, 0.2, 0.2, 1.0 ]
	}

}
