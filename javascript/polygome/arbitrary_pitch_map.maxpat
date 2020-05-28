{
	"patcher" : 	{
		"fileversion" : 1,
		"rect" : [ 468.0, 44.0, 606.0, 358.0 ],
		"bglocked" : 0,
		"defrect" : [ 468.0, 44.0, 606.0, 358.0 ],
		"openrect" : [ 0.0, 0.0, 0.0, 0.0 ],
		"openinpresentation" : 1,
		"default_fontsize" : 9.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 0,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 0,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"boxes" : [ 			{
				"box" : 				{
					"maxclass" : "inlet",
					"outlettype" : [ "" ],
					"numinlets" : 0,
					"patching_rect" : [ 196.0, 26.0, 25.0, 25.0 ],
					"id" : "obj-518",
					"numoutlets" : 1,
					"comment" : ""
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 255",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-3",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[255]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-4",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[256]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 254",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-5",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[254]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-6",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[255]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 253",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-7",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[253]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-8",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[254]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 252",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-9",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[252]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-10",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[253]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 251",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-11",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[251]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-12",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[252]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 250",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-13",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[250]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-14",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[251]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 249",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-15",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[249]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-16",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[250]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 248",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-17",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[248]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-18",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[249]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 247",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-19",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[247]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-20",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[248]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 246",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-21",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[246]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-22",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[247]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 245",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-23",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[245]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-24",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[246]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 244",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-25",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[244]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-26",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[245]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 243",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-27",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[243]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-28",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[244]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 242",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-29",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[242]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-30",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[243]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 241",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-31",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[241]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-32",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[242]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 240",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 666.0, 41.0, 17.0 ],
					"id" : "obj-33",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[240]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 328.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 649.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-34",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[241]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 239",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-35",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[239]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-36",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[240]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 238",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-37",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[238]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-38",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[239]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 237",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-39",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[237]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-40",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[238]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 236",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-41",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[236]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-42",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[237]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 235",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-43",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[235]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-44",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[236]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 234",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-45",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[234]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-46",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[235]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 233",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-47",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[233]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-48",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[234]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 232",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-49",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[232]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-50",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[233]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 231",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-51",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[231]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-52",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[232]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 230",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-53",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[230]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-54",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[231]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 229",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-55",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[229]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-56",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[230]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 228",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-57",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[228]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-58",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[229]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 227",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-59",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[227]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-60",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[228]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 226",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-61",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[226]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-62",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[227]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 225",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-63",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[225]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-64",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[226]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 224",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 631.0, 41.0, 17.0 ],
					"id" : "obj-65",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[224]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 308.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 614.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-66",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[225]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 223",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-67",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[223]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-68",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[224]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 222",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-69",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[222]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-70",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[223]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 221",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-71",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[221]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-72",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[222]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 220",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-73",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[220]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-74",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[221]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 219",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-75",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[219]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-76",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[220]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 218",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-77",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[218]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-78",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[219]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 217",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-79",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[217]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-80",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[218]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 216",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-81",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[216]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-82",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[217]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 215",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-83",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[215]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-84",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[216]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 214",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-85",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[214]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-86",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[215]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 213",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-87",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[213]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-88",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[214]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 212",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-89",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[212]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-90",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[213]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 211",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-91",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[211]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-92",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[212]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 210",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-93",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[210]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-94",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[211]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 209",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-95",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[209]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-96",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[210]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 208",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 596.0, 41.0, 17.0 ],
					"id" : "obj-97",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[208]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 288.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 579.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-98",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[209]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 207",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-99",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[207]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-100",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[208]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 206",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-101",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[206]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-102",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[207]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 205",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-103",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[205]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-104",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[206]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 204",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-105",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[204]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-106",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[205]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 203",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-107",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[203]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-108",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[204]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 202",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-109",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[202]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-110",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[203]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 201",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-111",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[201]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-112",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[202]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 200",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-113",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[200]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-114",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[201]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 199",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-115",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[199]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-116",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[200]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 198",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-117",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[198]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-118",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[199]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 197",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-119",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[197]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-120",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[198]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 196",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-121",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[196]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-122",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[197]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 195",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-123",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[195]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-124",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[196]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 194",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-125",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[194]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-126",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[195]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 193",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-127",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[193]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-128",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[194]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 192",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 561.0, 41.0, 17.0 ],
					"id" : "obj-129",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[192]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 268.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 544.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-130",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[193]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 191",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-131",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[191]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-132",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[192]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 190",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-133",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[190]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-134",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[191]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 189",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-135",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[189]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-136",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[190]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 188",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-137",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[188]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-138",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[189]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 187",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-139",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[187]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-140",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[188]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 186",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-141",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[186]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-142",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[187]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 185",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-143",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[185]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-144",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[186]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 184",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-145",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[184]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-146",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[185]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 183",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-147",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[183]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-148",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[184]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 182",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-149",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[182]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-150",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[183]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 181",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-151",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[181]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-152",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[182]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 180",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-153",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[180]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-154",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[181]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 179",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-155",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[179]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-156",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[180]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 178",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-157",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[178]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-158",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[179]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 177",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-159",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[177]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-160",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[178]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 176",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 517.0, 41.0, 17.0 ],
					"id" : "obj-161",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[176]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 242.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 500.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-162",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[177]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 175",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-163",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[175]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-164",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[176]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 174",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-165",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[174]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-166",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[175]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 173",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-167",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[173]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-168",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[174]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 172",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-169",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[172]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-170",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[173]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 171",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-171",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[171]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-172",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[172]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 170",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-173",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[170]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-174",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[171]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 169",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-175",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[169]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-176",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[170]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 168",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-177",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[168]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-178",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[169]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 167",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-179",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[167]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-180",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[168]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 166",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-181",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[166]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-182",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[167]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 165",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-183",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[165]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-184",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[166]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 164",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-185",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[164]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-186",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[165]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 163",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-187",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[163]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-188",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[164]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 162",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-189",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[162]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-190",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[163]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 161",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-191",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[161]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-192",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[162]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 160",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 482.0, 41.0, 17.0 ],
					"id" : "obj-193",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[160]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 222.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 465.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-194",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[161]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 159",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-195",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[159]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-196",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[160]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 158",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-197",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[158]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-198",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[159]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 157",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-199",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[157]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-200",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[158]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 156",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-201",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[156]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-202",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[157]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 155",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-203",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[155]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-204",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[156]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 154",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-205",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[154]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-206",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[155]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 153",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-207",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[153]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-208",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[154]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 152",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-209",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[152]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-210",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[153]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 151",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-211",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[151]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-212",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[152]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 150",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-213",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[150]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-214",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[151]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 149",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-215",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[149]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-216",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[150]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 148",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-217",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[148]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-218",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[149]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 147",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-219",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[147]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-220",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[148]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 146",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-221",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[146]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-222",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[147]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 145",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-223",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[145]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-224",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[146]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 144",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 447.0, 41.0, 17.0 ],
					"id" : "obj-225",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[144]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 202.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 430.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-226",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[145]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 143",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-227",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[143]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-228",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[144]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 142",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-229",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[142]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-230",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[143]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 141",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-231",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[141]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-232",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[142]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 140",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-233",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[140]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-234",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[141]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 139",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-235",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[139]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-236",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[140]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 138",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-237",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[138]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-238",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[139]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 137",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-239",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[137]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-240",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[138]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 136",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-241",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[136]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-242",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[137]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 135",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-243",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[135]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-244",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[136]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 134",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-245",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[134]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-246",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[135]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 133",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-247",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[133]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-248",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[134]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 132",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-249",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[132]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-250",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[133]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 131",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-251",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[131]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-252",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[132]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 130",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-253",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[130]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-254",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[131]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 129",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-255",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[129]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-256",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[130]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 128",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 412.0, 41.0, 17.0 ],
					"id" : "obj-257",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[128]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 182.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 395.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-258",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[129]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 127",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-259",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[127]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-260",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[128]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 126",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-261",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[126]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-262",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[127]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 125",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-263",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[125]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-264",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[126]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 124",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-265",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[124]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-266",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[125]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 123",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-267",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[123]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-268",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[124]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 122",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-269",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[122]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-270",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[123]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 121",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-271",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[121]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-272",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[122]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 120",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-273",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[120]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-274",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[121]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 119",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-275",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[119]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-276",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[120]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 118",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-277",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[118]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-278",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[119]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 117",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-279",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[117]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-280",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[118]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 116",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-281",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[116]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-282",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[117]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 115",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-283",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[115]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-284",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[116]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 114",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-285",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[114]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-286",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[115]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 113",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-287",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[113]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-288",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[114]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 112",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 357.0, 41.0, 17.0 ],
					"id" : "obj-289",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[112]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 157.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 340.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-290",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[113]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 111",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-291",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[111]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-292",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[112]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 110",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-293",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[110]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-294",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[111]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 109",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-295",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[109]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-296",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[110]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 108",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-297",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[108]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-298",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[109]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 107",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-299",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[107]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-300",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[108]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 106",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-301",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[106]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-302",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[107]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 105",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-303",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[105]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-304",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[106]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 104",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-305",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[104]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-306",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[105]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 103",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-307",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[103]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-308",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[104]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 102",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-309",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[102]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-310",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[103]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 101",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-311",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[101]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-312",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[102]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 100",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 322.0, 41.0, 17.0 ],
					"id" : "obj-313",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[100]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-314",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[101]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 99",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 322.0, 35.0, 17.0 ],
					"id" : "obj-315",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[99]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-316",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[100]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 98",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 322.0, 35.0, 17.0 ],
					"id" : "obj-317",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[98]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-318",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[99]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 97",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 322.0, 35.0, 17.0 ],
					"id" : "obj-319",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[97]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-320",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[98]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 96",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 322.0, 35.0, 17.0 ],
					"id" : "obj-321",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[96]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 137.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 305.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-322",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[97]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 95",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-323",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[95]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-324",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[96]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 94",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-325",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[94]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-326",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[95]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 93",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-327",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[93]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-328",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[94]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 92",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-329",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[92]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-330",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[93]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 91",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-331",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[91]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-332",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[92]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 90",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-333",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[90]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-334",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[91]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 89",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-335",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[89]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-336",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[90]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 88",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-337",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[88]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-338",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[89]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 87",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-339",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[87]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-340",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[88]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 86",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-341",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[86]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-342",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[87]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 85",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-343",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[85]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-344",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[86]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 84",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-345",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[84]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-346",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[85]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 83",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-347",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[83]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-348",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[84]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 82",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-349",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[82]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-350",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[83]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 81",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-351",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[81]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-352",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[82]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 80",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 287.0, 35.0, 17.0 ],
					"id" : "obj-353",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[80]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 117.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 270.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-354",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[81]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 79",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-355",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[79]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-356",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[80]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 78",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-357",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[78]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-358",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[79]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 77",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-359",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[77]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-360",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[78]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 76",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-361",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[76]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-362",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[77]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 75",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-363",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[75]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-364",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[76]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 74",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-365",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[74]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-366",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[75]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 73",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-367",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[73]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-368",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[74]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 72",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-369",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[72]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-370",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[73]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 71",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-371",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[71]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-372",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[72]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 70",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-373",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[70]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-374",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[71]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 69",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-375",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[69]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-376",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[70]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 68",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-377",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[68]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-378",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[69]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 67",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-379",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[67]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-380",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[68]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 66",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-381",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[66]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-382",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[67]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 65",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-383",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[65]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-384",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[66]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 64",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 252.0, 35.0, 17.0 ],
					"id" : "obj-385",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[64]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 97.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 235.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-386",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[65]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 63",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-387",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[63]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-388",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[64]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 62",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-389",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[62]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-390",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[63]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 61",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-391",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[61]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-392",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[62]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 60",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-393",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[60]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-394",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[61]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 59",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-395",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[59]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-396",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[60]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 58",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-397",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[58]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-398",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[59]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 57",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-399",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[57]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-400",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[58]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 56",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-401",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[56]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-402",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[57]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 55",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-403",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[55]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-404",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[56]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 54",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-405",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[54]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-406",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[55]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 53",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-407",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[53]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-408",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[54]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 52",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-409",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[52]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-410",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[53]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 51",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-411",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[51]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-412",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[52]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 50",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-413",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[50]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-414",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[51]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 49",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-415",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[49]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-416",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[50]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 48",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 208.0, 35.0, 17.0 ],
					"id" : "obj-417",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[48]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 71.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 191.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-418",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[49]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 47",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-419",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[47]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-420",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[48]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 46",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-421",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[46]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-422",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[47]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 45",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-423",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[45]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-424",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[46]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 44",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-425",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[44]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-426",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[45]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 43",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-427",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[43]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-428",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[44]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 42",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-429",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[42]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-430",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[43]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 41",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-431",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[41]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-432",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[42]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 40",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-433",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[40]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-434",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[41]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 39",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-435",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[39]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-436",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[40]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 38",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-437",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[38]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-438",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[39]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 37",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-439",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[37]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-440",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[38]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 36",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-441",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[36]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-442",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[37]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 35",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-443",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[35]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-444",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[36]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 34",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-445",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[34]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-446",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[35]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 33",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-447",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[33]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-448",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[34]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 32",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 173.0, 35.0, 17.0 ],
					"id" : "obj-449",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[32]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 51.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 156.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-450",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[33]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 31",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-451",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[31]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-452",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[32]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 30",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-453",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[30]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-454",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[31]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 29",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-455",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[29]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-456",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[30]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 28",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-457",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[28]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-458",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[29]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 27",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-459",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[27]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-460",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[28]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 26",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-461",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[26]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-462",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[27]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 25",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-463",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[25]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-464",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[26]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 24",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-465",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[24]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-466",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[25]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 23",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-467",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[23]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-468",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[24]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 22",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-469",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[22]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-470",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[23]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 21",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-471",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[21]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-472",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[22]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 20",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-473",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[20]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-474",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[21]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 19",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-475",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[19]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-476",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[20]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 18",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-477",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[18]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-478",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[19]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 17",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-479",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[17]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-480",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[18]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 16",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 138.0, 35.0, 17.0 ],
					"id" : "obj-481",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[16]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 31.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 121.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-482",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[17]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 15",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-483",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[15]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 562.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 562.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-484",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[16]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 14",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-485",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[14]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 526.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 526.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-486",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[15]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 13",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-487",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[13]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 490.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 490.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-488",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[14]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 12",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-489",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[12]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 454.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 454.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-490",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[13]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 11",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-491",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[11]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 412.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 412.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-492",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[12]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 10",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 103.0, 35.0, 17.0 ],
					"id" : "obj-493",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[10]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 376.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 376.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-494",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[11]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 9",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-495",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[9]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 340.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 340.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-496",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[10]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 8",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-497",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[8]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 304.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 304.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-498",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[9]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 7",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-499",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[7]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 261.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 261.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-500",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[8]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 6",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-501",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[6]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 225.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 225.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-502",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[7]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 5",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-503",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[5]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 189.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 189.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-504",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[6]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 4",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-505",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[4]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 153.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-506",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[5]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 3",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-507",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[3]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 111.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 111.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-508",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[4]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 2",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-509",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[2]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 75.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 75.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-510",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[3]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 1",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-511",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox[1]",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 39.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 39.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-512",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[2]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "r ---arbmappg",
					"outlettype" : [ "" ],
					"fontsize" : 9.0,
					"numinlets" : 0,
					"patching_rect" : [ 109.0, 25.0, 66.0, 17.0 ],
					"id" : "obj-513",
					"fontname" : "Arial",
					"numoutlets" : 1,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "ap 0",
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 103.0, 29.0, 17.0 ],
					"id" : "obj-514",
					"fontname" : "Arial",
					"numoutlets" : 0,
					"hidden" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "live.numbox",
					"varname" : "live.numbox",
					"outlettype" : [ "", "float" ],
					"presentation_rect" : [ 3.0, 11.0, 36.0, 15.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 3.0, 86.0, 36.0, 15.0 ],
					"presentation" : 1,
					"id" : "obj-515",
					"parameter_enable" : 1,
					"numoutlets" : 2,
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "arbmap[1]",
							"parameter_modmin" : 0.0,
							"parameter_linknames" : 0,
							"parameter_modmode" : 0,
							"parameter_info" : "",
							"parameter_order" : 0,
							"parameter_units" : "",
							"parameter_speedlim" : 0,
							"parameter_steps" : 0,
							"parameter_exponent" : 1.0,
							"parameter_unitstyle" : 8,
							"parameter_mmax" : 127.0,
							"parameter_mmin" : 0.0,
							"parameter_type" : 1,
							"parameter_initial_enable" : 0,
							"parameter_shortname" : "arbmap[1]",
							"parameter_invisible" : 1,
							"parameter_modmax" : 127.0,
							"parameter_annotation_name" : ""
						}

					}

				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "coll arbmap",
					"outlettype" : [ "", "", "", "" ],
					"fontsize" : 9.0,
					"numinlets" : 1,
					"patching_rect" : [ 109.0, 49.0, 62.0, 17.0 ],
					"id" : "obj-516",
					"fontname" : "Arial",
					"numoutlets" : 4,
					"hidden" : 1,
					"saved_object_attributes" : 					{
						"embed" : 0
					}

				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"source" : [ "obj-4", 0 ],
					"destination" : [ "obj-3", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-6", 0 ],
					"destination" : [ "obj-5", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-8", 0 ],
					"destination" : [ "obj-7", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-10", 0 ],
					"destination" : [ "obj-9", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-12", 0 ],
					"destination" : [ "obj-11", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-14", 0 ],
					"destination" : [ "obj-13", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-16", 0 ],
					"destination" : [ "obj-15", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-18", 0 ],
					"destination" : [ "obj-17", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-20", 0 ],
					"destination" : [ "obj-19", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-22", 0 ],
					"destination" : [ "obj-21", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-24", 0 ],
					"destination" : [ "obj-23", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-26", 0 ],
					"destination" : [ "obj-25", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-28", 0 ],
					"destination" : [ "obj-27", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-30", 0 ],
					"destination" : [ "obj-29", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-32", 0 ],
					"destination" : [ "obj-31", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-34", 0 ],
					"destination" : [ "obj-33", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-36", 0 ],
					"destination" : [ "obj-35", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-38", 0 ],
					"destination" : [ "obj-37", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-40", 0 ],
					"destination" : [ "obj-39", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-42", 0 ],
					"destination" : [ "obj-41", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-44", 0 ],
					"destination" : [ "obj-43", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-46", 0 ],
					"destination" : [ "obj-45", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-48", 0 ],
					"destination" : [ "obj-47", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-50", 0 ],
					"destination" : [ "obj-49", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-52", 0 ],
					"destination" : [ "obj-51", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-54", 0 ],
					"destination" : [ "obj-53", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-56", 0 ],
					"destination" : [ "obj-55", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-58", 0 ],
					"destination" : [ "obj-57", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-60", 0 ],
					"destination" : [ "obj-59", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-62", 0 ],
					"destination" : [ "obj-61", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-64", 0 ],
					"destination" : [ "obj-63", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-66", 0 ],
					"destination" : [ "obj-65", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-68", 0 ],
					"destination" : [ "obj-67", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-70", 0 ],
					"destination" : [ "obj-69", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-72", 0 ],
					"destination" : [ "obj-71", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-74", 0 ],
					"destination" : [ "obj-73", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-76", 0 ],
					"destination" : [ "obj-75", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-78", 0 ],
					"destination" : [ "obj-77", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-80", 0 ],
					"destination" : [ "obj-79", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-82", 0 ],
					"destination" : [ "obj-81", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-84", 0 ],
					"destination" : [ "obj-83", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-86", 0 ],
					"destination" : [ "obj-85", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-88", 0 ],
					"destination" : [ "obj-87", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-90", 0 ],
					"destination" : [ "obj-89", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-92", 0 ],
					"destination" : [ "obj-91", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-94", 0 ],
					"destination" : [ "obj-93", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-96", 0 ],
					"destination" : [ "obj-95", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-98", 0 ],
					"destination" : [ "obj-97", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-100", 0 ],
					"destination" : [ "obj-99", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-102", 0 ],
					"destination" : [ "obj-101", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-104", 0 ],
					"destination" : [ "obj-103", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-106", 0 ],
					"destination" : [ "obj-105", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-108", 0 ],
					"destination" : [ "obj-107", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-110", 0 ],
					"destination" : [ "obj-109", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-112", 0 ],
					"destination" : [ "obj-111", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-114", 0 ],
					"destination" : [ "obj-113", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-116", 0 ],
					"destination" : [ "obj-115", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-118", 0 ],
					"destination" : [ "obj-117", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-120", 0 ],
					"destination" : [ "obj-119", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-122", 0 ],
					"destination" : [ "obj-121", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-124", 0 ],
					"destination" : [ "obj-123", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-126", 0 ],
					"destination" : [ "obj-125", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-128", 0 ],
					"destination" : [ "obj-127", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-130", 0 ],
					"destination" : [ "obj-129", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-132", 0 ],
					"destination" : [ "obj-131", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-134", 0 ],
					"destination" : [ "obj-133", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-136", 0 ],
					"destination" : [ "obj-135", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-138", 0 ],
					"destination" : [ "obj-137", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-140", 0 ],
					"destination" : [ "obj-139", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-142", 0 ],
					"destination" : [ "obj-141", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-144", 0 ],
					"destination" : [ "obj-143", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-146", 0 ],
					"destination" : [ "obj-145", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-148", 0 ],
					"destination" : [ "obj-147", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-150", 0 ],
					"destination" : [ "obj-149", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-152", 0 ],
					"destination" : [ "obj-151", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-154", 0 ],
					"destination" : [ "obj-153", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-156", 0 ],
					"destination" : [ "obj-155", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-158", 0 ],
					"destination" : [ "obj-157", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-160", 0 ],
					"destination" : [ "obj-159", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-162", 0 ],
					"destination" : [ "obj-161", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-164", 0 ],
					"destination" : [ "obj-163", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-166", 0 ],
					"destination" : [ "obj-165", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-168", 0 ],
					"destination" : [ "obj-167", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-170", 0 ],
					"destination" : [ "obj-169", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-172", 0 ],
					"destination" : [ "obj-171", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-174", 0 ],
					"destination" : [ "obj-173", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-176", 0 ],
					"destination" : [ "obj-175", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-178", 0 ],
					"destination" : [ "obj-177", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-180", 0 ],
					"destination" : [ "obj-179", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-182", 0 ],
					"destination" : [ "obj-181", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-184", 0 ],
					"destination" : [ "obj-183", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-186", 0 ],
					"destination" : [ "obj-185", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-188", 0 ],
					"destination" : [ "obj-187", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-190", 0 ],
					"destination" : [ "obj-189", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-192", 0 ],
					"destination" : [ "obj-191", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-194", 0 ],
					"destination" : [ "obj-193", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-196", 0 ],
					"destination" : [ "obj-195", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-198", 0 ],
					"destination" : [ "obj-197", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-200", 0 ],
					"destination" : [ "obj-199", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-202", 0 ],
					"destination" : [ "obj-201", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-204", 0 ],
					"destination" : [ "obj-203", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-206", 0 ],
					"destination" : [ "obj-205", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-208", 0 ],
					"destination" : [ "obj-207", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-210", 0 ],
					"destination" : [ "obj-209", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-212", 0 ],
					"destination" : [ "obj-211", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-214", 0 ],
					"destination" : [ "obj-213", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-216", 0 ],
					"destination" : [ "obj-215", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-218", 0 ],
					"destination" : [ "obj-217", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-220", 0 ],
					"destination" : [ "obj-219", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-222", 0 ],
					"destination" : [ "obj-221", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-224", 0 ],
					"destination" : [ "obj-223", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-226", 0 ],
					"destination" : [ "obj-225", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-228", 0 ],
					"destination" : [ "obj-227", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-230", 0 ],
					"destination" : [ "obj-229", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-232", 0 ],
					"destination" : [ "obj-231", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-234", 0 ],
					"destination" : [ "obj-233", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-236", 0 ],
					"destination" : [ "obj-235", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-238", 0 ],
					"destination" : [ "obj-237", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-240", 0 ],
					"destination" : [ "obj-239", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-242", 0 ],
					"destination" : [ "obj-241", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-244", 0 ],
					"destination" : [ "obj-243", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-246", 0 ],
					"destination" : [ "obj-245", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-248", 0 ],
					"destination" : [ "obj-247", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-250", 0 ],
					"destination" : [ "obj-249", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-252", 0 ],
					"destination" : [ "obj-251", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-254", 0 ],
					"destination" : [ "obj-253", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-256", 0 ],
					"destination" : [ "obj-255", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-258", 0 ],
					"destination" : [ "obj-257", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-260", 0 ],
					"destination" : [ "obj-259", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-262", 0 ],
					"destination" : [ "obj-261", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-264", 0 ],
					"destination" : [ "obj-263", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-266", 0 ],
					"destination" : [ "obj-265", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-268", 0 ],
					"destination" : [ "obj-267", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-270", 0 ],
					"destination" : [ "obj-269", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-272", 0 ],
					"destination" : [ "obj-271", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-274", 0 ],
					"destination" : [ "obj-273", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-276", 0 ],
					"destination" : [ "obj-275", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-278", 0 ],
					"destination" : [ "obj-277", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-280", 0 ],
					"destination" : [ "obj-279", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-282", 0 ],
					"destination" : [ "obj-281", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-284", 0 ],
					"destination" : [ "obj-283", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-286", 0 ],
					"destination" : [ "obj-285", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-288", 0 ],
					"destination" : [ "obj-287", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-290", 0 ],
					"destination" : [ "obj-289", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-292", 0 ],
					"destination" : [ "obj-291", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-294", 0 ],
					"destination" : [ "obj-293", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-296", 0 ],
					"destination" : [ "obj-295", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-298", 0 ],
					"destination" : [ "obj-297", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-300", 0 ],
					"destination" : [ "obj-299", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-302", 0 ],
					"destination" : [ "obj-301", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-304", 0 ],
					"destination" : [ "obj-303", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-306", 0 ],
					"destination" : [ "obj-305", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-308", 0 ],
					"destination" : [ "obj-307", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-310", 0 ],
					"destination" : [ "obj-309", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-312", 0 ],
					"destination" : [ "obj-311", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-314", 0 ],
					"destination" : [ "obj-313", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-316", 0 ],
					"destination" : [ "obj-315", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-318", 0 ],
					"destination" : [ "obj-317", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-320", 0 ],
					"destination" : [ "obj-319", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-322", 0 ],
					"destination" : [ "obj-321", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-324", 0 ],
					"destination" : [ "obj-323", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-326", 0 ],
					"destination" : [ "obj-325", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-328", 0 ],
					"destination" : [ "obj-327", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-330", 0 ],
					"destination" : [ "obj-329", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-332", 0 ],
					"destination" : [ "obj-331", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-334", 0 ],
					"destination" : [ "obj-333", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-336", 0 ],
					"destination" : [ "obj-335", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-338", 0 ],
					"destination" : [ "obj-337", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-340", 0 ],
					"destination" : [ "obj-339", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-342", 0 ],
					"destination" : [ "obj-341", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-344", 0 ],
					"destination" : [ "obj-343", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-346", 0 ],
					"destination" : [ "obj-345", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-348", 0 ],
					"destination" : [ "obj-347", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-350", 0 ],
					"destination" : [ "obj-349", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-352", 0 ],
					"destination" : [ "obj-351", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-354", 0 ],
					"destination" : [ "obj-353", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-356", 0 ],
					"destination" : [ "obj-355", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-358", 0 ],
					"destination" : [ "obj-357", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-360", 0 ],
					"destination" : [ "obj-359", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-362", 0 ],
					"destination" : [ "obj-361", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-364", 0 ],
					"destination" : [ "obj-363", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-366", 0 ],
					"destination" : [ "obj-365", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-368", 0 ],
					"destination" : [ "obj-367", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-370", 0 ],
					"destination" : [ "obj-369", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-372", 0 ],
					"destination" : [ "obj-371", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-374", 0 ],
					"destination" : [ "obj-373", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-376", 0 ],
					"destination" : [ "obj-375", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-378", 0 ],
					"destination" : [ "obj-377", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-380", 0 ],
					"destination" : [ "obj-379", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-382", 0 ],
					"destination" : [ "obj-381", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-384", 0 ],
					"destination" : [ "obj-383", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-386", 0 ],
					"destination" : [ "obj-385", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-388", 0 ],
					"destination" : [ "obj-387", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-390", 0 ],
					"destination" : [ "obj-389", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-392", 0 ],
					"destination" : [ "obj-391", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-394", 0 ],
					"destination" : [ "obj-393", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-396", 0 ],
					"destination" : [ "obj-395", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-398", 0 ],
					"destination" : [ "obj-397", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-400", 0 ],
					"destination" : [ "obj-399", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-402", 0 ],
					"destination" : [ "obj-401", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-404", 0 ],
					"destination" : [ "obj-403", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-406", 0 ],
					"destination" : [ "obj-405", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-408", 0 ],
					"destination" : [ "obj-407", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-410", 0 ],
					"destination" : [ "obj-409", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-412", 0 ],
					"destination" : [ "obj-411", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-414", 0 ],
					"destination" : [ "obj-413", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-416", 0 ],
					"destination" : [ "obj-415", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-418", 0 ],
					"destination" : [ "obj-417", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-420", 0 ],
					"destination" : [ "obj-419", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-422", 0 ],
					"destination" : [ "obj-421", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-424", 0 ],
					"destination" : [ "obj-423", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-426", 0 ],
					"destination" : [ "obj-425", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-428", 0 ],
					"destination" : [ "obj-427", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-430", 0 ],
					"destination" : [ "obj-429", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-432", 0 ],
					"destination" : [ "obj-431", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-434", 0 ],
					"destination" : [ "obj-433", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-436", 0 ],
					"destination" : [ "obj-435", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-438", 0 ],
					"destination" : [ "obj-437", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-440", 0 ],
					"destination" : [ "obj-439", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-442", 0 ],
					"destination" : [ "obj-441", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-444", 0 ],
					"destination" : [ "obj-443", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-446", 0 ],
					"destination" : [ "obj-445", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-448", 0 ],
					"destination" : [ "obj-447", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-450", 0 ],
					"destination" : [ "obj-449", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-452", 0 ],
					"destination" : [ "obj-451", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-454", 0 ],
					"destination" : [ "obj-453", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-456", 0 ],
					"destination" : [ "obj-455", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-458", 0 ],
					"destination" : [ "obj-457", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-460", 0 ],
					"destination" : [ "obj-459", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-462", 0 ],
					"destination" : [ "obj-461", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-464", 0 ],
					"destination" : [ "obj-463", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-466", 0 ],
					"destination" : [ "obj-465", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-468", 0 ],
					"destination" : [ "obj-467", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-470", 0 ],
					"destination" : [ "obj-469", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-472", 0 ],
					"destination" : [ "obj-471", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-474", 0 ],
					"destination" : [ "obj-473", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-476", 0 ],
					"destination" : [ "obj-475", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-478", 0 ],
					"destination" : [ "obj-477", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-480", 0 ],
					"destination" : [ "obj-479", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-482", 0 ],
					"destination" : [ "obj-481", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-484", 0 ],
					"destination" : [ "obj-483", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-486", 0 ],
					"destination" : [ "obj-485", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-488", 0 ],
					"destination" : [ "obj-487", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-490", 0 ],
					"destination" : [ "obj-489", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-492", 0 ],
					"destination" : [ "obj-491", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-494", 0 ],
					"destination" : [ "obj-493", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-496", 0 ],
					"destination" : [ "obj-495", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-498", 0 ],
					"destination" : [ "obj-497", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-500", 0 ],
					"destination" : [ "obj-499", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-502", 0 ],
					"destination" : [ "obj-501", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-504", 0 ],
					"destination" : [ "obj-503", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-506", 0 ],
					"destination" : [ "obj-505", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-508", 0 ],
					"destination" : [ "obj-507", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-510", 0 ],
					"destination" : [ "obj-509", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-512", 0 ],
					"destination" : [ "obj-511", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-515", 0 ],
					"destination" : [ "obj-514", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-513", 0 ],
					"destination" : [ "obj-516", 0 ],
					"hidden" : 1,
					"midpoints" : [  ]
				}

			}
 ],
		"parameters" : 		{
			"obj-486" : [ "arbmap[15]", "arbmap[1]", 0 ],
			"obj-318" : [ "arbmap[99]", "arbmap[1]", 0 ],
			"obj-200" : [ "arbmap[158]", "arbmap[1]", 0 ],
			"obj-82" : [ "arbmap[217]", "arbmap[1]", 0 ],
			"obj-472" : [ "arbmap[22]", "arbmap[1]", 0 ],
			"obj-308" : [ "arbmap[104]", "arbmap[1]", 0 ],
			"obj-190" : [ "arbmap[163]", "arbmap[1]", 0 ],
			"obj-72" : [ "arbmap[222]", "arbmap[1]", 0 ],
			"obj-462" : [ "arbmap[27]", "arbmap[1]", 0 ],
			"obj-298" : [ "arbmap[109]", "arbmap[1]", 0 ],
			"obj-182" : [ "arbmap[167]", "arbmap[1]", 0 ],
			"obj-452" : [ "arbmap[32]", "arbmap[1]", 0 ],
			"obj-288" : [ "arbmap[114]", "arbmap[1]", 0 ],
			"obj-176" : [ "arbmap[170]", "arbmap[1]", 0 ],
			"obj-448" : [ "arbmap[34]", "arbmap[1]", 0 ],
			"obj-278" : [ "arbmap[119]", "arbmap[1]", 0 ],
			"obj-160" : [ "arbmap[178]", "arbmap[1]", 0 ],
			"obj-70" : [ "arbmap[223]", "arbmap[1]", 0 ],
			"obj-432" : [ "arbmap[42]", "arbmap[1]", 0 ],
			"obj-386" : [ "arbmap[65]", "arbmap[1]", 0 ],
			"obj-268" : [ "arbmap[124]", "arbmap[1]", 0 ],
			"obj-150" : [ "arbmap[183]", "arbmap[1]", 0 ],
			"obj-60" : [ "arbmap[228]", "arbmap[1]", 0 ],
			"obj-422" : [ "arbmap[47]", "arbmap[1]", 0 ],
			"obj-376" : [ "arbmap[70]", "arbmap[1]", 0 ],
			"obj-258" : [ "arbmap[129]", "arbmap[1]", 0 ],
			"obj-140" : [ "arbmap[188]", "arbmap[1]", 0 ],
			"obj-50" : [ "arbmap[233]", "arbmap[1]", 0 ],
			"obj-412" : [ "arbmap[52]", "arbmap[1]", 0 ],
			"obj-366" : [ "arbmap[75]", "arbmap[1]", 0 ],
			"obj-248" : [ "arbmap[134]", "arbmap[1]", 0 ],
			"obj-130" : [ "arbmap[193]", "arbmap[1]", 0 ],
			"obj-40" : [ "arbmap[238]", "arbmap[1]", 0 ],
			"obj-402" : [ "arbmap[57]", "arbmap[1]", 0 ],
			"obj-358" : [ "arbmap[79]", "arbmap[1]", 0 ],
			"obj-238" : [ "arbmap[139]", "arbmap[1]", 0 ],
			"obj-120" : [ "arbmap[198]", "arbmap[1]", 0 ],
			"obj-30" : [ "arbmap[243]", "arbmap[1]", 0 ],
			"obj-510" : [ "arbmap[3]", "arbmap[1]", 0 ],
			"obj-392" : [ "arbmap[62]", "arbmap[1]", 0 ],
			"obj-352" : [ "arbmap[82]", "arbmap[1]", 0 ],
			"obj-228" : [ "arbmap[144]", "arbmap[1]", 0 ],
			"obj-110" : [ "arbmap[203]", "arbmap[1]", 0 ],
			"obj-20" : [ "arbmap[248]", "arbmap[1]", 0 ],
			"obj-506" : [ "arbmap[5]", "arbmap[1]", 0 ],
			"obj-336" : [ "arbmap[90]", "arbmap[1]", 0 ],
			"obj-218" : [ "arbmap[149]", "arbmap[1]", 0 ],
			"obj-100" : [ "arbmap[208]", "arbmap[1]", 0 ],
			"obj-10" : [ "arbmap[253]", "arbmap[1]", 0 ],
			"obj-488" : [ "arbmap[14]", "arbmap[1]", 0 ],
			"obj-326" : [ "arbmap[95]", "arbmap[1]", 0 ],
			"obj-208" : [ "arbmap[154]", "arbmap[1]", 0 ],
			"obj-90" : [ "arbmap[213]", "arbmap[1]", 0 ],
			"obj-478" : [ "arbmap[19]", "arbmap[1]", 0 ],
			"obj-316" : [ "arbmap[100]", "arbmap[1]", 0 ],
			"obj-198" : [ "arbmap[159]", "arbmap[1]", 0 ],
			"obj-80" : [ "arbmap[218]", "arbmap[1]", 0 ],
			"obj-470" : [ "arbmap[23]", "arbmap[1]", 0 ],
			"obj-306" : [ "arbmap[105]", "arbmap[1]", 0 ],
			"obj-188" : [ "arbmap[164]", "arbmap[1]", 0 ],
			"obj-460" : [ "arbmap[28]", "arbmap[1]", 0 ],
			"obj-296" : [ "arbmap[110]", "arbmap[1]", 0 ],
			"obj-184" : [ "arbmap[166]", "arbmap[1]", 0 ],
			"obj-450" : [ "arbmap[33]", "arbmap[1]", 0 ],
			"obj-286" : [ "arbmap[115]", "arbmap[1]", 0 ],
			"obj-168" : [ "arbmap[174]", "arbmap[1]", 0 ],
			"obj-436" : [ "arbmap[40]", "arbmap[1]", 0 ],
			"obj-276" : [ "arbmap[120]", "arbmap[1]", 0 ],
			"obj-158" : [ "arbmap[179]", "arbmap[1]", 0 ],
			"obj-68" : [ "arbmap[224]", "arbmap[1]", 0 ],
			"obj-430" : [ "arbmap[43]", "arbmap[1]", 0 ],
			"obj-384" : [ "arbmap[66]", "arbmap[1]", 0 ],
			"obj-266" : [ "arbmap[125]", "arbmap[1]", 0 ],
			"obj-148" : [ "arbmap[184]", "arbmap[1]", 0 ],
			"obj-58" : [ "arbmap[229]", "arbmap[1]", 0 ],
			"obj-420" : [ "arbmap[48]", "arbmap[1]", 0 ],
			"obj-374" : [ "arbmap[71]", "arbmap[1]", 0 ],
			"obj-256" : [ "arbmap[130]", "arbmap[1]", 0 ],
			"obj-138" : [ "arbmap[189]", "arbmap[1]", 0 ],
			"obj-48" : [ "arbmap[234]", "arbmap[1]", 0 ],
			"obj-410" : [ "arbmap[53]", "arbmap[1]", 0 ],
			"obj-364" : [ "arbmap[76]", "arbmap[1]", 0 ],
			"obj-246" : [ "arbmap[135]", "arbmap[1]", 0 ],
			"obj-128" : [ "arbmap[194]", "arbmap[1]", 0 ],
			"obj-38" : [ "arbmap[239]", "arbmap[1]", 0 ],
			"obj-400" : [ "arbmap[58]", "arbmap[1]", 0 ],
			"obj-360" : [ "arbmap[78]", "arbmap[1]", 0 ],
			"obj-236" : [ "arbmap[140]", "arbmap[1]", 0 ],
			"obj-118" : [ "arbmap[199]", "arbmap[1]", 0 ],
			"obj-28" : [ "arbmap[244]", "arbmap[1]", 0 ],
			"obj-512" : [ "arbmap[2]", "arbmap[1]", 0 ],
			"obj-344" : [ "arbmap[86]", "arbmap[1]", 0 ],
			"obj-226" : [ "arbmap[145]", "arbmap[1]", 0 ],
			"obj-108" : [ "arbmap[204]", "arbmap[1]", 0 ],
			"obj-18" : [ "arbmap[249]", "arbmap[1]", 0 ],
			"obj-498" : [ "arbmap[9]", "arbmap[1]", 0 ],
			"obj-334" : [ "arbmap[91]", "arbmap[1]", 0 ],
			"obj-216" : [ "arbmap[150]", "arbmap[1]", 0 ],
			"obj-98" : [ "arbmap[209]", "arbmap[1]", 0 ],
			"obj-8" : [ "arbmap[254]", "arbmap[1]", 0 ],
			"obj-490" : [ "arbmap[13]", "arbmap[1]", 0 ],
			"obj-324" : [ "arbmap[96]", "arbmap[1]", 0 ],
			"obj-206" : [ "arbmap[155]", "arbmap[1]", 0 ],
			"obj-88" : [ "arbmap[214]", "arbmap[1]", 0 ],
			"obj-484" : [ "arbmap[16]", "arbmap[1]", 0 ],
			"obj-314" : [ "arbmap[101]", "arbmap[1]", 0 ],
			"obj-196" : [ "arbmap[160]", "arbmap[1]", 0 ],
			"obj-78" : [ "arbmap[219]", "arbmap[1]", 0 ],
			"obj-468" : [ "arbmap[24]", "arbmap[1]", 0 ],
			"obj-304" : [ "arbmap[106]", "arbmap[1]", 0 ],
			"obj-186" : [ "arbmap[165]", "arbmap[1]", 0 ],
			"obj-458" : [ "arbmap[29]", "arbmap[1]", 0 ],
			"obj-294" : [ "arbmap[111]", "arbmap[1]", 0 ],
			"obj-172" : [ "arbmap[172]", "arbmap[1]", 0 ],
			"obj-438" : [ "arbmap[39]", "arbmap[1]", 0 ],
			"obj-284" : [ "arbmap[116]", "arbmap[1]", 0 ],
			"obj-166" : [ "arbmap[175]", "arbmap[1]", 0 ],
			"obj-442" : [ "arbmap[37]", "arbmap[1]", 0 ],
			"obj-274" : [ "arbmap[121]", "arbmap[1]", 0 ],
			"obj-156" : [ "arbmap[180]", "arbmap[1]", 0 ],
			"obj-66" : [ "arbmap[225]", "arbmap[1]", 0 ],
			"obj-428" : [ "arbmap[44]", "arbmap[1]", 0 ],
			"obj-382" : [ "arbmap[67]", "arbmap[1]", 0 ],
			"obj-264" : [ "arbmap[126]", "arbmap[1]", 0 ],
			"obj-146" : [ "arbmap[185]", "arbmap[1]", 0 ],
			"obj-56" : [ "arbmap[230]", "arbmap[1]", 0 ],
			"obj-418" : [ "arbmap[49]", "arbmap[1]", 0 ],
			"obj-372" : [ "arbmap[72]", "arbmap[1]", 0 ],
			"obj-254" : [ "arbmap[131]", "arbmap[1]", 0 ],
			"obj-136" : [ "arbmap[190]", "arbmap[1]", 0 ],
			"obj-46" : [ "arbmap[235]", "arbmap[1]", 0 ],
			"obj-408" : [ "arbmap[54]", "arbmap[1]", 0 ],
			"obj-362" : [ "arbmap[77]", "arbmap[1]", 0 ],
			"obj-244" : [ "arbmap[136]", "arbmap[1]", 0 ],
			"obj-126" : [ "arbmap[195]", "arbmap[1]", 0 ],
			"obj-36" : [ "arbmap[240]", "arbmap[1]", 0 ],
			"obj-398" : [ "arbmap[59]", "arbmap[1]", 0 ],
			"obj-348" : [ "arbmap[84]", "arbmap[1]", 0 ],
			"obj-234" : [ "arbmap[141]", "arbmap[1]", 0 ],
			"obj-116" : [ "arbmap[200]", "arbmap[1]", 0 ],
			"obj-26" : [ "arbmap[245]", "arbmap[1]", 0 ],
			"obj-502" : [ "arbmap[7]", "arbmap[1]", 0 ],
			"obj-342" : [ "arbmap[87]", "arbmap[1]", 0 ],
			"obj-224" : [ "arbmap[146]", "arbmap[1]", 0 ],
			"obj-106" : [ "arbmap[205]", "arbmap[1]", 0 ],
			"obj-16" : [ "arbmap[250]", "arbmap[1]", 0 ],
			"obj-496" : [ "arbmap[10]", "arbmap[1]", 0 ],
			"obj-332" : [ "arbmap[92]", "arbmap[1]", 0 ],
			"obj-214" : [ "arbmap[151]", "arbmap[1]", 0 ],
			"obj-96" : [ "arbmap[210]", "arbmap[1]", 0 ],
			"obj-6" : [ "arbmap[255]", "arbmap[1]", 0 ],
			"obj-492" : [ "arbmap[12]", "arbmap[1]", 0 ],
			"obj-322" : [ "arbmap[97]", "arbmap[1]", 0 ],
			"obj-204" : [ "arbmap[156]", "arbmap[1]", 0 ],
			"obj-86" : [ "arbmap[215]", "arbmap[1]", 0 ],
			"obj-476" : [ "arbmap[20]", "arbmap[1]", 0 ],
			"obj-312" : [ "arbmap[102]", "arbmap[1]", 0 ],
			"obj-194" : [ "arbmap[161]", "arbmap[1]", 0 ],
			"obj-76" : [ "arbmap[220]", "arbmap[1]", 0 ],
			"obj-466" : [ "arbmap[25]", "arbmap[1]", 0 ],
			"obj-302" : [ "arbmap[107]", "arbmap[1]", 0 ],
			"obj-174" : [ "arbmap[171]", "arbmap[1]", 0 ],
			"obj-456" : [ "arbmap[30]", "arbmap[1]", 0 ],
			"obj-292" : [ "arbmap[112]", "arbmap[1]", 0 ],
			"obj-178" : [ "arbmap[169]", "arbmap[1]", 0 ],
			"obj-444" : [ "arbmap[36]", "arbmap[1]", 0 ],
			"obj-282" : [ "arbmap[117]", "arbmap[1]", 0 ],
			"obj-164" : [ "arbmap[176]", "arbmap[1]", 0 ],
			"obj-434" : [ "arbmap[41]", "arbmap[1]", 0 ],
			"obj-390" : [ "arbmap[63]", "arbmap[1]", 0 ],
			"obj-272" : [ "arbmap[122]", "arbmap[1]", 0 ],
			"obj-154" : [ "arbmap[181]", "arbmap[1]", 0 ],
			"obj-64" : [ "arbmap[226]", "arbmap[1]", 0 ],
			"obj-515" : [ "arbmap[1]", "arbmap[1]", 0 ],
			"obj-426" : [ "arbmap[45]", "arbmap[1]", 0 ],
			"obj-380" : [ "arbmap[68]", "arbmap[1]", 0 ],
			"obj-262" : [ "arbmap[127]", "arbmap[1]", 0 ],
			"obj-144" : [ "arbmap[186]", "arbmap[1]", 0 ],
			"obj-54" : [ "arbmap[231]", "arbmap[1]", 0 ],
			"obj-416" : [ "arbmap[50]", "arbmap[1]", 0 ],
			"obj-370" : [ "arbmap[73]", "arbmap[1]", 0 ],
			"obj-252" : [ "arbmap[132]", "arbmap[1]", 0 ],
			"obj-134" : [ "arbmap[191]", "arbmap[1]", 0 ],
			"obj-44" : [ "arbmap[236]", "arbmap[1]", 0 ],
			"obj-406" : [ "arbmap[55]", "arbmap[1]", 0 ],
			"obj-350" : [ "arbmap[83]", "arbmap[1]", 0 ],
			"obj-242" : [ "arbmap[137]", "arbmap[1]", 0 ],
			"obj-124" : [ "arbmap[196]", "arbmap[1]", 0 ],
			"obj-34" : [ "arbmap[241]", "arbmap[1]", 0 ],
			"obj-396" : [ "arbmap[60]", "arbmap[1]", 0 ],
			"obj-354" : [ "arbmap[81]", "arbmap[1]", 0 ],
			"obj-232" : [ "arbmap[142]", "arbmap[1]", 0 ],
			"obj-114" : [ "arbmap[201]", "arbmap[1]", 0 ],
			"obj-24" : [ "arbmap[246]", "arbmap[1]", 0 ],
			"obj-508" : [ "arbmap[4]", "arbmap[1]", 0 ],
			"obj-340" : [ "arbmap[88]", "arbmap[1]", 0 ],
			"obj-222" : [ "arbmap[147]", "arbmap[1]", 0 ],
			"obj-104" : [ "arbmap[206]", "arbmap[1]", 0 ],
			"obj-14" : [ "arbmap[251]", "arbmap[1]", 0 ],
			"obj-494" : [ "arbmap[11]", "arbmap[1]", 0 ],
			"obj-330" : [ "arbmap[93]", "arbmap[1]", 0 ],
			"obj-212" : [ "arbmap[152]", "arbmap[1]", 0 ],
			"obj-94" : [ "arbmap[211]", "arbmap[1]", 0 ],
			"obj-4" : [ "arbmap[256]", "arbmap[1]", 0 ],
			"obj-480" : [ "arbmap[18]", "arbmap[1]", 0 ],
			"obj-320" : [ "arbmap[98]", "arbmap[1]", 0 ],
			"obj-202" : [ "arbmap[157]", "arbmap[1]", 0 ],
			"obj-84" : [ "arbmap[216]", "arbmap[1]", 0 ],
			"obj-474" : [ "arbmap[21]", "arbmap[1]", 0 ],
			"obj-310" : [ "arbmap[103]", "arbmap[1]", 0 ],
			"obj-192" : [ "arbmap[162]", "arbmap[1]", 0 ],
			"obj-74" : [ "arbmap[221]", "arbmap[1]", 0 ],
			"obj-464" : [ "arbmap[26]", "arbmap[1]", 0 ],
			"obj-300" : [ "arbmap[108]", "arbmap[1]", 0 ],
			"obj-180" : [ "arbmap[168]", "arbmap[1]", 0 ],
			"obj-454" : [ "arbmap[31]", "arbmap[1]", 0 ],
			"obj-290" : [ "arbmap[113]", "arbmap[1]", 0 ],
			"obj-170" : [ "arbmap[173]", "arbmap[1]", 0 ],
			"obj-446" : [ "arbmap[35]", "arbmap[1]", 0 ],
			"obj-280" : [ "arbmap[118]", "arbmap[1]", 0 ],
			"obj-162" : [ "arbmap[177]", "arbmap[1]", 0 ],
			"obj-440" : [ "arbmap[38]", "arbmap[1]", 0 ],
			"obj-388" : [ "arbmap[64]", "arbmap[1]", 0 ],
			"obj-270" : [ "arbmap[123]", "arbmap[1]", 0 ],
			"obj-152" : [ "arbmap[182]", "arbmap[1]", 0 ],
			"obj-62" : [ "arbmap[227]", "arbmap[1]", 0 ],
			"obj-424" : [ "arbmap[46]", "arbmap[1]", 0 ],
			"obj-378" : [ "arbmap[69]", "arbmap[1]", 0 ],
			"obj-260" : [ "arbmap[128]", "arbmap[1]", 0 ],
			"obj-142" : [ "arbmap[187]", "arbmap[1]", 0 ],
			"obj-52" : [ "arbmap[232]", "arbmap[1]", 0 ],
			"obj-414" : [ "arbmap[51]", "arbmap[1]", 0 ],
			"obj-368" : [ "arbmap[74]", "arbmap[1]", 0 ],
			"obj-250" : [ "arbmap[133]", "arbmap[1]", 0 ],
			"obj-132" : [ "arbmap[192]", "arbmap[1]", 0 ],
			"obj-42" : [ "arbmap[237]", "arbmap[1]", 0 ],
			"obj-404" : [ "arbmap[56]", "arbmap[1]", 0 ],
			"obj-356" : [ "arbmap[80]", "arbmap[1]", 0 ],
			"obj-240" : [ "arbmap[138]", "arbmap[1]", 0 ],
			"obj-122" : [ "arbmap[197]", "arbmap[1]", 0 ],
			"obj-32" : [ "arbmap[242]", "arbmap[1]", 0 ],
			"obj-504" : [ "arbmap[6]", "arbmap[1]", 0 ],
			"obj-394" : [ "arbmap[61]", "arbmap[1]", 0 ],
			"obj-346" : [ "arbmap[85]", "arbmap[1]", 0 ],
			"obj-230" : [ "arbmap[143]", "arbmap[1]", 0 ],
			"obj-112" : [ "arbmap[202]", "arbmap[1]", 0 ],
			"obj-22" : [ "arbmap[247]", "arbmap[1]", 0 ],
			"obj-500" : [ "arbmap[8]", "arbmap[1]", 0 ],
			"obj-338" : [ "arbmap[89]", "arbmap[1]", 0 ],
			"obj-220" : [ "arbmap[148]", "arbmap[1]", 0 ],
			"obj-102" : [ "arbmap[207]", "arbmap[1]", 0 ],
			"obj-12" : [ "arbmap[252]", "arbmap[1]", 0 ],
			"obj-482" : [ "arbmap[17]", "arbmap[1]", 0 ],
			"obj-328" : [ "arbmap[94]", "arbmap[1]", 0 ],
			"obj-210" : [ "arbmap[153]", "arbmap[1]", 0 ],
			"obj-92" : [ "arbmap[212]", "arbmap[1]", 0 ]
		}

	}

}
