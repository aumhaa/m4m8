{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 6,
			"minor" : 1,
			"revision" : 8,
			"architecture" : "x86"
		}
,
		"rect" : [ 0.0, 44.0, 868.0, 496.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Andale Mono",
		"gridonopen" : 0,
		"gridsize" : [ 16.0, 16.0 ],
		"gridsnaponopen" : 0,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"boxes" : [ 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-2",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 372.0, 146.0, 150.0, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 331.0, 145.0, 187.0, 20.0 ],
					"text" : "mod_b996 port by amounra"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-3",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 376.0, 11.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 12.0,
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 377.0, 41.0, 90.0, 20.0 ],
					"save" : [ "#N", "thispatcher", ";", "#Q", "end", ";" ],
					"text" : "thispatcher"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-42",
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 71.0, 62.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-41",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 15.0, 3.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-29",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 32.0, 688.0, 150.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 105.0, 146.0, 150.0, 20.0 ],
					"text" : "http://monome.org"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-27",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 32.0, 672.0, 150.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 105.0, 130.0, 150.0, 20.0 ],
					"text" : "august 2010 by tehn"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 30.0,
					"frgb" : 0.0,
					"id" : "obj-24",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 32.0, 656.0, 315.0, 40.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 4.0, 126.0, 66.0, 40.0 ],
					"text" : "xor"
				}

			}
, 			{
				"box" : 				{
					"args" : [ 7, "---7" ],
					"id" : "obj-19",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 912.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 604.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 6, "---6" ],
					"id" : "obj-18",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 784.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 518.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 5, "---5" ],
					"id" : "obj-17",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 656.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 432.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 4, "---4" ],
					"id" : "obj-16",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 528.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 346.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 3, "---3" ],
					"id" : "obj-14",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 400.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 260.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 2, "---2" ],
					"id" : "obj-13",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 272.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 174.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 1, "---1" ],
					"id" : "obj-12",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 144.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 88.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"args" : [ 0, "---0" ],
					"id" : "obj-10",
					"maxclass" : "bpatcher",
					"name" : "_xor_part.maxpat",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 16.0, 240.0, 124.0, 251.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 2.0, 1.0, 85.0, 129.0 ]
				}

			}
, 			{
				"box" : 				{
					"align" : 1,
					"arrow" : 0,
					"arrowbgcolor" : [ 1.0, 1.0, 1.0, 0.0 ],
					"arrowframe" : 0,
					"arrowlink" : 0,
					"fontname" : "Andale Mono",
					"fontsize" : 24.0,
					"hltcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"id" : "obj-44",
					"ignoreclick" : 1,
					"items" : [ "value", ",", "link" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 15.0, 93.0, 267.0, 33.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 525.0, 132.0, 165.0, 33.0 ],
					"rounded" : 0
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Andale Mono",
					"fontsize" : 12.0,
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "int", "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 6,
							"minor" : 1,
							"revision" : 8,
							"architecture" : "x86"
						}
,
						"rect" : [ 172.0, 98.0, 1018.0, 665.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Andale Mono",
						"gridonopen" : 0,
						"gridsize" : [ 16.0, 16.0 ],
						"gridsnaponopen" : 0,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"boxanimatetime" : 200,
						"imprint" : 0,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"boxes" : [ 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-19",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 228.0, 141.0, 32.5, 18.0 ],
									"text" : "1"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-17",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 190.0, 140.0, 32.5, 18.0 ],
									"text" : "0"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-10",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "bang", "bang", "" ],
									"patching_rect" : [ 191.0, 106.0, 83.0, 20.0 ],
									"text" : "select 1 2"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-5",
									"maxclass" : "newobj",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 191.0, 67.0, 83.0, 20.0 ],
									"text" : "r ---keyin"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-3",
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 367.0, 548.0, 25.0, 25.0 ]
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-24",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "bang", "bang", "" ],
									"patching_rect" : [ 127.0, 335.0, 61.0, 20.0 ],
									"text" : "sel 0 1"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-16",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 79.0, 399.0, 119.0, 20.0 ],
									"text" : "s ---update-len"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-12",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 111.0, 431.0, 126.0, 20.0 ],
									"text" : "s ---update-link"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-49",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 719.0, 367.0, 61.0, 20.0 ],
									"text" : "route 1"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-48",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 719.0, 335.0, 68.0, 18.0 ],
									"text" : "$3 $1 $2"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-40",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 511.0, 303.0, 155.0, 20.0 ],
									"text" : "prepend /xor/led_col"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-41",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 479.0, 271.0, 126.0, 20.0 ],
									"text" : "prepend /xor/led"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-42",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 479.0, 239.0, 104.0, 20.0 ],
									"text" : "route led col"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-43",
									"maxclass" : "newobj",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 479.0, 207.0, 90.0, 20.0 ],
									"text" : "r ---l-link"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-39",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 694.0, 514.0, 90.0, 20.0 ],
									"text" : "s ---k-link"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-38",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 575.0, 511.0, 83.0, 20.0 ],
									"text" : "s ---k-len"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-37",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 575.0, 479.0, 54.0, 20.0 ],
									"text" : "gate 2"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-35",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 207.0, 335.0, 32.5, 20.0 ],
									"text" : "+ 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-34",
									"maxclass" : "toggle",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 191.0, 271.0, 55.0, 55.0 ]
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-31",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 367.0, 479.0, 68.0, 20.0 ],
									"text" : "switch 2"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-30",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 735.0, 431.0, 134.0, 18.0 ],
									"text" : "0 7"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-23",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 319.0, 303.0, 155.0, 20.0 ],
									"text" : "prepend /xor/led_col"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-22",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 287.0, 271.0, 126.0, 20.0 ],
									"text" : "prepend /xor/led"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-21",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 287.0, 239.0, 104.0, 20.0 ],
									"text" : "route led col"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-20",
									"maxclass" : "newobj",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 287.0, 207.0, 83.0, 20.0 ],
									"text" : "r ---l-len"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Andale Mono",
									"fontsize" : 12.0,
									"id" : "obj-18",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 367.0, 511.0, 111.0, 20.0 ],
									"saved_object_attributes" : 									{
										"filename" : "monolink.js",
										"parameter_enable" : 0
									}
,
									"text" : "js monolink.js"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-2",
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 176.0, 528.0, 25.0, 25.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-1",
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 719.0, 267.0, 25.0, 25.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-48", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-1", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-17", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-10", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-19", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-10", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-34", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-17", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-3", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-18", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-34", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-19", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-21", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-20", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-22", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-21", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-23", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-21", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-22", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-23", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-12", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-24", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-16", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-24", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-18", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-31", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-2", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-34", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-24", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-34", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-35", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-34", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-35", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-37", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-35", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-38", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-37", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-39", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-37", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 2 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-40", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 2 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-41", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-40", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-42", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-41", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-42", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-42", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-43", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-49", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-48", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-49", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-37", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-49", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-10", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-5", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 15.0, 34.0, 75.0, 20.0 ],
					"saved_object_attributes" : 					{
						"default_fontface" : 0,
						"default_fontname" : "Andale Mono",
						"default_fontsize" : 12.0,
						"description" : "",
						"digest" : "",
						"fontface" : 0,
						"fontname" : "Andale Mono",
						"fontsize" : 12.0,
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p routing"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-8", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-44", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-8", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-10::obj-122" : [ "matrixctrl", "matrixctrl", 0 ],
			"obj-13::obj-37::obj-7" : [ "duration[5]", "duration", 0 ],
			"obj-13::obj-67" : [ "type[5]", "type", 0 ],
			"obj-19::obj-37::obj-21" : [ "c_mute", "c_mute", 0 ],
			"obj-14::obj-33" : [ "number[7]", "number[1]", 0 ],
			"obj-16::obj-37::obj-21" : [ "c_mute[3]", "c_mute", 0 ],
			"obj-19::obj-33" : [ "number[14]", "number[1]", 0 ],
			"obj-16::obj-122" : [ "matrixctrl[9]", "matrixctrl", 0 ],
			"obj-17::obj-37::obj-5" : [ "note[2]", "note", 0 ],
			"obj-13::obj-112" : [ "matrixctrl[4]", "matrixctrl[1]", 0 ],
			"obj-18::obj-37::obj-12" : [ "velocity[1]", "velocity", 0 ],
			"obj-10::obj-67" : [ "type[7]", "type", 0 ],
			"obj-18::obj-68" : [ "num[1]", "num", 0 ],
			"obj-18::obj-59" : [ "number[12]", "number", 0 ],
			"obj-12::obj-33" : [ "number[2]", "number[1]", 0 ],
			"obj-17::obj-33" : [ "number[11]", "number[1]", 0 ],
			"obj-13::obj-37::obj-5" : [ "note[5]", "note", 0 ],
			"obj-17::obj-112" : [ "matrixctrl[10]", "matrixctrl[1]", 0 ],
			"obj-10::obj-59" : [ "number", "number", 0 ],
			"obj-13::obj-59" : [ "number[4]", "number", 0 ],
			"obj-16::obj-37::obj-5" : [ "note[3]", "note", 0 ],
			"obj-19::obj-37::obj-5" : [ "note", "note", 0 ],
			"obj-14::obj-37::obj-21" : [ "c_mute[4]", "c_mute", 0 ],
			"obj-16::obj-33" : [ "number[9]", "number[1]", 0 ],
			"obj-14::obj-122" : [ "matrixctrl[6]", "matrixctrl", 0 ],
			"obj-19::obj-37::obj-7" : [ "duration", "duration", 0 ],
			"obj-14::obj-68" : [ "num[4]", "num", 0 ],
			"obj-17::obj-37::obj-7" : [ "duration[2]", "duration", 0 ],
			"obj-10::obj-37::obj-21" : [ "c_mute[7]", "c_mute", 0 ],
			"obj-17::obj-67" : [ "type[2]", "type", 0 ],
			"obj-19::obj-67" : [ "type", "type", 0 ],
			"obj-18::obj-37::obj-7" : [ "duration[1]", "duration", 0 ],
			"obj-19::obj-112" : [ "matrixctrl[15]", "matrixctrl[1]", 0 ],
			"obj-12::obj-37::obj-12" : [ "velocity[6]", "velocity", 0 ],
			"obj-12::obj-112" : [ "matrixctrl[3]", "matrixctrl[1]", 0 ],
			"obj-12::obj-122" : [ "matrixctrl[2]", "matrixctrl", 0 ],
			"obj-18::obj-122" : [ "matrixctrl[13]", "matrixctrl", 0 ],
			"obj-14::obj-59" : [ "number[6]", "number", 0 ],
			"obj-13::obj-37::obj-21" : [ "c_mute[5]", "c_mute", 0 ],
			"obj-13::obj-68" : [ "num[5]", "num", 0 ],
			"obj-16::obj-37::obj-7" : [ "duration[3]", "duration", 0 ],
			"obj-14::obj-37::obj-12" : [ "velocity[4]", "velocity", 0 ],
			"obj-14::obj-112" : [ "matrixctrl[7]", "matrixctrl[1]", 0 ],
			"obj-16::obj-67" : [ "type[3]", "type", 0 ],
			"obj-19::obj-59" : [ "number[15]", "number", 0 ],
			"obj-14::obj-67" : [ "type[4]", "type", 0 ],
			"obj-10::obj-37::obj-5" : [ "note[7]", "note", 0 ],
			"obj-17::obj-68" : [ "num[2]", "num", 0 ],
			"obj-10::obj-68" : [ "num[7]", "num", 0 ],
			"obj-18::obj-37::obj-21" : [ "c_mute[1]", "c_mute", 0 ],
			"obj-19::obj-68" : [ "num", "num", 0 ],
			"obj-12::obj-37::obj-5" : [ "note[6]", "note", 0 ],
			"obj-17::obj-59" : [ "number[10]", "number", 0 ],
			"obj-12::obj-68" : [ "num[6]", "num", 0 ],
			"obj-18::obj-112" : [ "matrixctrl[12]", "matrixctrl[1]", 0 ],
			"obj-13::obj-37::obj-12" : [ "velocity[5]", "velocity", 0 ],
			"obj-14::obj-37::obj-5" : [ "note[4]", "note", 0 ],
			"obj-16::obj-68" : [ "num[3]", "num", 0 ],
			"obj-16::obj-59" : [ "number[8]", "number", 0 ],
			"obj-17::obj-37::obj-21" : [ "c_mute[2]", "c_mute", 0 ],
			"obj-19::obj-37::obj-12" : [ "velocity", "velocity", 0 ],
			"obj-10::obj-37::obj-7" : [ "duration[7]", "duration", 0 ],
			"obj-18::obj-37::obj-5" : [ "note[1]", "note", 0 ],
			"obj-12::obj-37::obj-7" : [ "duration[6]", "duration", 0 ],
			"obj-13::obj-33" : [ "number[5]", "number[1]", 0 ],
			"obj-12::obj-67" : [ "type[6]", "type", 0 ],
			"obj-17::obj-122" : [ "matrixctrl[11]", "matrixctrl", 0 ],
			"obj-16::obj-37::obj-12" : [ "velocity[3]", "velocity", 0 ],
			"obj-18::obj-33" : [ "number[13]", "number[1]", 0 ],
			"obj-14::obj-37::obj-7" : [ "duration[4]", "duration", 0 ],
			"obj-10::obj-112" : [ "matrixctrl[1]", "matrixctrl[1]", 0 ],
			"obj-16::obj-112" : [ "matrixctrl[8]", "matrixctrl[1]", 0 ],
			"obj-17::obj-37::obj-12" : [ "velocity[2]", "velocity", 0 ],
			"obj-10::obj-37::obj-12" : [ "velocity[7]", "velocity", 0 ],
			"obj-13::obj-122" : [ "matrixctrl[5]", "matrixctrl", 0 ],
			"obj-19::obj-122" : [ "matrixctrl[14]", "matrixctrl", 0 ],
			"obj-18::obj-67" : [ "type[1]", "type", 0 ],
			"obj-12::obj-37::obj-21" : [ "c_mute[6]", "c_mute", 0 ],
			"obj-10::obj-33" : [ "number[1]", "number[1]", 0 ],
			"obj-12::obj-59" : [ "number[3]", "number", 0 ]
		}
,
		"dependency_cache" : [ 			{
				"name" : "monolink.js",
				"bootpath" : "/Users/amounra/Documents/Max/Packages/mod/javascript/xor",
				"patcherrelativepath" : ".",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "_xor_part.maxpat",
				"bootpath" : "/Users/amounra/Documents/Max/Packages/mod/javascript/xor",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "_xor_midi.maxpat",
				"bootpath" : "/Users/amounra/Documents/Max/Packages/mod/javascript/xor",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
 ]
	}

}
