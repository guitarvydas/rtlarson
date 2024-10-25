

counter =  0                                                                    #line 1
                                                                                #line 2

digits = [                                                                      #line 3
"₀", "₁", "₂", "₃", "₄", "₅",                                                   #line 4
"₆", "₇", "₈", "₉",                                                             #line 5
"₁₀", "₁₁", "₁₂", "₁₃", "₁₄",                                                   #line 6
"₁₅", "₁₆", "₁₇", "₁₈", "₁₉",                                                   #line 7
"₂₀", "₂₁", "₂₂", "₂₃", "₂₄",                                                   #line 8
"₂₅", "₂₆", "₂₇", "₂₈", "₂₉"]                                                   #line 9
                                                                                #line 10
                                                                                #line 11

def gensymbol (s):                                                              #line 12

    global counter                                                              #line 13

    name_with_id =  str( s) + subscripted_digit ( counter)                      #line 14

    counter =  counter+ 1                                                       #line 15

    return  name_with_id                                                        #line 16
                                                                                #line 17

                                                                                #line 18

def subscripted_digit (n):                                                      #line 19

    global digits                                                               #line 20

    if ( n >=  0 and  n <=  29):                                                #line 21

        return  digits [ n]                                                     #line 22

    else:                                                                       #line 23

        return  str( "₊") +  n                                                  #line 24
                                                                                #line 25

                                                                                #line 26

                                                                                #line 27

class Datum:
    def __init__ (self,):                                                       #line 28

        self.data =  None                                                       #line 29

        self.clone =  None                                                      #line 30

        self.reclaim =  None                                                    #line 31

        self.srepr =  None                                                      #line 32

        self.kind =  None                                                       #line 33

        self.raw =  None                                                        #line 34
                                                                                #line 35

                                                                                #line 36

def new_datum_string (s):                                                       #line 37

    d =  Datum ()                                                               #line 38

    d. data =  s                                                                #line 39

    d. clone =  lambda : clone_datum_string ( d)                                #line 40

    d. reclaim =  lambda : reclaim_datum_string ( d)                            #line 41

    d. srepr =  lambda : srepr_datum_string ( d)                                #line 42

    d. raw =  lambda : raw_datum_string ( d)                                    #line 43

    d. kind =  lambda :  "string"                                               #line 44

    return  d                                                                   #line 45
                                                                                #line 46

                                                                                #line 47

def clone_datum_string (d):                                                     #line 48

    d = new_datum_string ( d. data)                                             #line 49

    return  d                                                                   #line 50
                                                                                #line 51

                                                                                #line 52

def reclaim_datum_string (src):                                                 #line 53

    pass                                                                        #line 54
                                                                                #line 55

                                                                                #line 56

def srepr_datum_string (d):                                                     #line 57

    return  d. data                                                             #line 58
                                                                                #line 59

                                                                                #line 60

def raw_datum_string (d):                                                       #line 61

    return bytearray ( d. data, "UTF_8")                                        #line 62
                                                                                #line 63

                                                                                #line 64

def new_datum_bang ():                                                          #line 65

    p = Datum ()                                                                #line 66

    p. data =  True                                                             #line 67

    p. clone =  lambda : clone_datum_bang ( p)                                  #line 68

    p. reclaim =  lambda : reclaim_datum_bang ( p)                              #line 69

    p. srepr =  lambda : srepr_datum_bang ()                                    #line 70

    p. raw =  lambda : raw_datum_bang ()                                        #line 71

    p. kind =  lambda :  "bang"                                                 #line 72

    return  p                                                                   #line 73
                                                                                #line 74

                                                                                #line 75

def clone_datum_bang (d):                                                       #line 76

    return new_datum_bang ()                                                    #line 77
                                                                                #line 78

                                                                                #line 79

def reclaim_datum_bang (d):                                                     #line 80

    pass                                                                        #line 81
                                                                                #line 82

                                                                                #line 83

def srepr_datum_bang ():                                                        #line 84

    return  "!"                                                                 #line 85
                                                                                #line 86

                                                                                #line 87

def raw_datum_bang ():                                                          #line 88

    return []                                                                   #line 89
                                                                                #line 90

                                                                                #line 91

def new_datum_tick ():                                                          #line 92

    p = new_datum_bang ()                                                       #line 93

    p. kind =  lambda :  "tick"                                                 #line 94

    p. clone =  lambda : new_datum_tick ()                                      #line 95

    p. srepr =  lambda : srepr_datum_tick ()                                    #line 96

    p. raw =  lambda : raw_datum_tick ()                                        #line 97

    return  p                                                                   #line 98
                                                                                #line 99

                                                                                #line 100

def srepr_datum_tick ():                                                        #line 101

    return  "."                                                                 #line 102
                                                                                #line 103

                                                                                #line 104

def raw_datum_tick ():                                                          #line 105

    return []                                                                   #line 106
                                                                                #line 107

                                                                                #line 108

def new_datum_bytes (b):                                                        #line 109

    p = Datum ()                                                                #line 110

    p. data =  b                                                                #line 111

    p. clone =  lambda : clone_datum_bytes ( p)                                 #line 112

    p. reclaim =  lambda : reclaim_datum_bytes ( p)                             #line 113

    p. srepr =  lambda : srepr_datum_bytes ( b)                                 #line 114

    p. raw =  lambda : raw_datum_bytes ( b)                                     #line 115

    p. kind =  lambda :  "bytes"                                                #line 116

    return  p                                                                   #line 117
                                                                                #line 118

                                                                                #line 119

def clone_datum_bytes (src):                                                    #line 120

    p = Datum ()                                                                #line 121

    p =  src                                                                    #line 122

    p. data =  src.clone ()                                                     #line 123

    return  p                                                                   #line 124
                                                                                #line 125

                                                                                #line 126

def reclaim_datum_bytes (src):                                                  #line 127

    pass                                                                        #line 128
                                                                                #line 129

                                                                                #line 130

def srepr_datum_bytes (d):                                                      #line 131

    return  d. data.decode ( "UTF_8")                                           #line 132
                                                                                #line 133


def raw_datum_bytes (d):                                                        #line 134

    return  d. data                                                             #line 135
                                                                                #line 136

                                                                                #line 137

def new_datum_handle (h):                                                       #line 138

    return new_datum_int ( h)                                                   #line 139
                                                                                #line 140

                                                                                #line 141

def new_datum_int (i):                                                          #line 142

    p = Datum ()                                                                #line 143

    p. data =  i                                                                #line 144

    p. clone =  lambda : clone_int ( i)                                         #line 145

    p. reclaim =  lambda : reclaim_int ( i)                                     #line 146

    p. srepr =  lambda : srepr_datum_int ( i)                                   #line 147

    p. raw =  lambda : raw_datum_int ( i)                                       #line 148

    p. kind =  lambda :  "int"                                                  #line 149

    return  p                                                                   #line 150
                                                                                #line 151

                                                                                #line 152

def clone_int (i):                                                              #line 153

    p = new_datum_int ( i)                                                      #line 154

    return  p                                                                   #line 155
                                                                                #line 156

                                                                                #line 157

def reclaim_int (src):                                                          #line 158

    pass                                                                        #line 159
                                                                                #line 160

                                                                                #line 161

def srepr_datum_int (i):                                                        #line 162

    return str ( i)                                                             #line 163
                                                                                #line 164

                                                                                #line 165

def raw_datum_int (i):                                                          #line 166

    return  i                                                                   #line 167
                                                                                #line 168

                                                                                #line 169
# Message passed to a leaf component.                                           #line 170
#                                                                               #line 171
# `port` refers to the name of the incoming or outgoing port of this component. #line 172
# `datum` is the data attached to this message.                                 #line 173

class Message:
    def __init__ (self,port,datum):                                             #line 174

        self.port =  port                                                       #line 175

        self.datum =  datum                                                     #line 176
                                                                                #line 177

                                                                                #line 178

def clone_port (s):                                                             #line 179

    return clone_string ( s)                                                    #line 180
                                                                                #line 181

                                                                                #line 182
# Utility for making a `Message`. Used to safely “seed“ messages                #line 183
# entering the very top of a network.                                           #line 184

def make_message (port,datum):                                                  #line 185

    p = clone_string ( port)                                                    #line 186

    m = Message ( p, datum.clone ())                                            #line 187

    return  m                                                                   #line 188
                                                                                #line 189

                                                                                #line 190
# Clones a message. Primarily used internally for “fanning out“ a message to multiple destinations.#line 191

def message_clone (message):                                                    #line 192

    m = Message (clone_port ( message. port), message. datum.clone ())          #line 193

    return  m                                                                   #line 194
                                                                                #line 195

                                                                                #line 196
# Frees a message.                                                              #line 197

def destroy_message (msg):                                                      #line 198

    # during debug, dont destroy any message, since we want to trace messages, thus, we need to persist ancestor messages#line 199

    pass                                                                        #line 200
                                                                                #line 201

                                                                                #line 202

def destroy_datum (msg):                                                        #line 203

    pass                                                                        #line 204
                                                                                #line 205

                                                                                #line 206

def destroy_port (msg):                                                         #line 207

    pass                                                                        #line 208
                                                                                #line 209

                                                                                #line 210
#                                                                               #line 211

def format_message (m):                                                         #line 212

    if  m ==  None:                                                             #line 213

        return  "ϕ"                                                             #line 214

    else:                                                                       #line 215

        return  str( "⟪") +  str( m. port) +  str( "⦂") +  str( m. datum.srepr ()) +  "⟫"    #line 219
                                                                                #line 220

                                                                                #line 221

                                                                                #line 222
                                                                                #line 223

enumDown =  0                                                                   #line 224

enumAcross =  1                                                                 #line 225

enumUp =  2                                                                     #line 226

enumThrough =  3                                                                #line 227
                                                                                #line 228

def container_instantiator (reg,owner,container_name,desc):                     #line 229

    global enumDown, enumUp, enumAcross, enumThrough                            #line 230

    container = make_container ( container_name, owner)                         #line 231

    children = []                                                               #line 232

    children_by_id = {}
    # not strictly necessary, but, we can remove 1 runtime lookup by “compiling it out“ here#line 233

    # collect children                                                          #line 234

    for child_desc in  desc ["children"]:                                       #line 235

        child_instance = get_component_instance ( reg, child_desc ["name"], container)#line 236

        children.append ( child_instance)                                       #line 237

        children_by_id [ child_desc ["id"]] =  child_instance                   #line 238


    container. children =  children                                             #line 239

    me =  container                                                             #line 240
                                                                                #line 241

    connectors = []                                                             #line 242

    for proto_conn in  desc ["connections"]:                                    #line 243

        source_component =  None                                                #line 244

        target_component =  None                                                #line 245

        connector = Connector ()                                                #line 246

        if  proto_conn ["dir"] ==  enumDown:                                    #line 247

            # JSON: {;dir': 0, 'source': {'name': '', 'id': 0}, 'source_port': '', 'target': {'name': 'Echo', 'id': 12}, 'target_port': ''},#line 248

            connector. direction =  "down"                                      #line 249

            connector. sender = Sender ( me. name, me, proto_conn ["source_port"])#line 250

            target_component =  children_by_id [ proto_conn ["target"] ["id"]]  #line 251

            if ( target_component ==  None):                                    #line 252

                load_error ( str( "internal error: .Down connection target internal error ") +  proto_conn ["target"] )#line 253

            else:                                                               #line 254

                connector. receiver = Receiver ( target_component. name, target_component. inq, proto_conn ["target_port"], target_component)#line 255

                connectors.append ( connector)
                                                                                #line 256

        elif  proto_conn ["dir"] ==  enumAcross:                                #line 257

            connector. direction =  "across"                                    #line 258

            source_component =  children_by_id [ proto_conn ["source"] ["id"]]  #line 259

            target_component =  children_by_id [ proto_conn ["target"] ["id"]]  #line 260

            if  source_component ==  None:                                      #line 261

                load_error ( str( "internal error: .Across connection source not ok ") +  proto_conn ["source"] )#line 262

            else:                                                               #line 263

                connector. sender = Sender ( source_component. name, source_component, proto_conn ["source_port"])#line 264

                if  target_component ==  None:                                  #line 265

                    load_error ( str( "internal error: .Across connection target not ok ") +  proto_conn. target )#line 266

                else:                                                           #line 267

                    connector. receiver = Receiver ( target_component. name, target_component. inq, proto_conn ["target_port"], target_component)#line 268

                    connectors.append ( connector)

                                                                                #line 269

        elif  proto_conn ["dir"] ==  enumUp:                                    #line 270

            connector. direction =  "up"                                        #line 271

            source_component =  children_by_id [ proto_conn ["source"] ["id"]]  #line 272

            if  source_component ==  None:                                      #line 273

                print ( str( "internal error: .Up connection source not ok ") +  proto_conn ["source"] )#line 274

            else:                                                               #line 275

                connector. sender = Sender ( source_component. name, source_component, proto_conn ["source_port"])#line 276

                connector. receiver = Receiver ( me. name, container. outq, proto_conn ["target_port"], me)#line 277

                connectors.append ( connector)
                                                                                #line 278

        elif  proto_conn ["dir"] ==  enumThrough:                               #line 279

            connector. direction =  "through"                                   #line 280

            connector. sender = Sender ( me. name, me, proto_conn ["source_port"])#line 281

            connector. receiver = Receiver ( me. name, container. outq, proto_conn ["target_port"], me)#line 282

            connectors.append ( connector)
                                                                                #line 283

                                                                                #line 284

    container. connections =  connectors                                        #line 285

    return  container                                                           #line 286
                                                                                #line 287

                                                                                #line 288
# The default handler for container components.                                 #line 289

def container_handler (container,message):                                      #line 290

    route ( container, container, message)
    # references to 'self' are replaced by the container during instantiation   #line 291

    while any_child_ready ( container):                                         #line 292

        step_children ( container, message)                                     #line 293

                                                                                #line 294

                                                                                #line 295
# Frees the given container and associated data.                                #line 296

def destroy_container (eh):                                                     #line 297

    pass                                                                        #line 298
                                                                                #line 299

                                                                                #line 300

def fifo_is_empty (fifo):                                                       #line 301

    return  fifo.empty ()                                                       #line 302
                                                                                #line 303

                                                                                #line 304
# Routing connection for a container component. The `direction` field has       #line 305
# no affect on the default message routing system _ it is there for debugging   #line 306
# purposes, or for reading by other tools.                                      #line 307
                                                                                #line 308

class Connector:
    def __init__ (self,):                                                       #line 309

        self.direction =  None # down, across, up, through                      #line 310

        self.sender =  None                                                     #line 311

        self.receiver =  None                                                   #line 312
                                                                                #line 313

                                                                                #line 314
# `Sender` is used to “pattern match“ which `Receiver` a message should go to,  #line 315
# based on component ID (pointer) and port name.                                #line 316
                                                                                #line 317

class Sender:
    def __init__ (self,name,component,port):                                    #line 318

        self.name =  name                                                       #line 319

        self.component =  component # from                                      #line 320

        self.port =  port # from's port                                         #line 321
                                                                                #line 322

                                                                                #line 323
# `Receiver` is a handle to a destination queue, and a `port` name to assign    #line 324
# to incoming messages to this queue.                                           #line 325
                                                                                #line 326

class Receiver:
    def __init__ (self,name,queue,port,component):                              #line 327

        self.name =  name                                                       #line 328

        self.queue =  queue # queue (input | output) of receiver                #line 329

        self.port =  port # destination port                                    #line 330

        self.component =  component # to (for bootstrap debug)                  #line 331
                                                                                #line 332

                                                                                #line 333
# Checks if two senders match, by pointer equality and port name matching.      #line 334

def sender_eq (s1,s2):                                                          #line 335

    same_components = ( s1. component ==  s2. component)                        #line 336

    same_ports = ( s1. port ==  s2. port)                                       #line 337

    return  same_components and  same_ports                                     #line 338
                                                                                #line 339

                                                                                #line 340
# Delivers the given message to the receiver of this connector.                 #line 341
                                                                                #line 342

def deposit (parent,conn,message):                                              #line 343

    new_message = make_message ( conn. receiver. port, message. datum)          #line 344

    push_message ( parent, conn. receiver. component, conn. receiver. queue, new_message)#line 345
                                                                                #line 346

                                                                                #line 347

def force_tick (parent,eh):                                                     #line 348

    tick_msg = make_message ( ".",new_datum_tick ())                            #line 349

    push_message ( parent, eh, eh. inq, tick_msg)                               #line 350

    return  tick_msg                                                            #line 351
                                                                                #line 352

                                                                                #line 353

def push_message (parent,receiver,inq,m):                                       #line 354

    inq.put ( m)                                                                #line 355

    parent. visit_ordering.put ( receiver)                                      #line 356
                                                                                #line 357

                                                                                #line 358

def is_self (child,container):                                                  #line 359

    # in an earlier version “self“ was denoted as ϕ                             #line 360

    return  child ==  container                                                 #line 361
                                                                                #line 362

                                                                                #line 363

def step_child (child,msg):                                                     #line 364

    before_state =  child. state                                                #line 365

    child.handler ( child, msg)                                                 #line 366

    after_state =  child. state                                                 #line 367

    return [ before_state ==  "idle" and  after_state!= "idle",                 #line 368
    before_state!= "idle" and  after_state!= "idle",                            #line 369
    before_state!= "idle" and  after_state ==  "idle"]                          #line 370
                                                                                #line 371

                                                                                #line 372

def save_message (eh,msg):                                                      #line 373

    eh. saved_messages.put ( msg)                                               #line 374
                                                                                #line 375

                                                                                #line 376

def fetch_saved_message_and_clear (eh):                                         #line 377

    return  eh. saved_messages.get ()                                           #line 378
                                                                                #line 379

                                                                                #line 380

def step_children (container,causingMessage):                                   #line 381

    container. state =  "idle"                                                  #line 382

    for child in list ( container. visit_ordering. queue):                      #line 383

        # child = container represents self, skip it                            #line 384

        if (not (is_self ( child, container))):                                 #line 385

            if (not ( child. inq.empty ())):                                    #line 386

                msg =  child. inq.get ()                                        #line 387

                [ began_long_run, continued_long_run, ended_long_run] = step_child ( child, msg)#line 388

                if  began_long_run:                                             #line 389

                    save_message ( child, msg)                                  #line 390

                elif  continued_long_run:                                       #line 391

                    pass                                                        #line 392
                                                                                #line 393


                destroy_message ( msg)                                          #line 394

            else:                                                               #line 395

                if  child. state!= "idle":                                      #line 396

                    msg = force_tick ( container, child)                        #line 397

                    child.handler ( child, msg)                                 #line 398

                    destroy_message ( msg)
                                                                                #line 399

                                                                                #line 400

            if  child. state ==  "active":                                      #line 401

                # if child remains active, then the container must remain active and must propagate “ticks“ to child#line 402

                container. state =  "active"                                    #line 403

                                                                                #line 404

            while (not ( child. outq.empty ())):                                #line 405

                msg =  child. outq.get ()                                       #line 406

                route ( container, child, msg)                                  #line 407

                destroy_message ( msg)

                                                                                #line 408

                                                                                #line 409
                                                                                #line 410
                                                                                #line 411

                                                                                #line 412

def attempt_tick (parent,eh):                                                   #line 413

    if  eh. state!= "idle":                                                     #line 414

        force_tick ( parent, eh)                                                #line 415

                                                                                #line 416

                                                                                #line 417

def is_tick (msg):                                                              #line 418

    return  "tick" ==  msg. datum.kind ()                                       #line 419
                                                                                #line 420

                                                                                #line 421
# Routes a single message to all matching destinations, according to            #line 422
# the container's connection network.                                           #line 423
                                                                                #line 424

def route (container,from_component,message):                                   #line 425

    was_sent =  False
    # for checking that output went somewhere (at least during bootstrap)       #line 426

    fromname =  ""                                                              #line 427

    if is_tick ( message):                                                      #line 428

        for child in  container. children:                                      #line 429

            attempt_tick ( container, child, message)                           #line 430


        was_sent =  True                                                        #line 431

    else:                                                                       #line 432

        if (not (is_self ( from_component, container))):                        #line 433

            fromname =  from_component. name                                    #line 434


        from_sender = Sender ( fromname, from_component, message. port)         #line 435
                                                                                #line 436

        for connector in  container. connections:                               #line 437

            if sender_eq ( from_sender, connector. sender):                     #line 438

                deposit ( container, connector, message)                        #line 439

                was_sent =  True

                                                                                #line 440


    if not ( was_sent):                                                         #line 441

        print ( "\n\n*** Error: ***")                                           #line 442

        dump_possible_connections ( container)                                  #line 443

        print_routing_trace ( container)                                        #line 444

        print ( "***")                                                          #line 445

        print ( str( container. name) +  str( ": message '") +  str( message. port) +  str( "' from ") +  str( fromname) +  " dropped on floor..."     )#line 446

        print ( "***")                                                          #line 447

        exit ()                                                                 #line 448

                                                                                #line 449

                                                                                #line 450

def dump_possible_connections (container):                                      #line 451

    print ( str( "*** possible connections for ") +  str( container. name) +  ":"  )#line 452

    for connector in  container. connections:                                   #line 453

        print ( str( connector. direction) +  str( " ") +  str( connector. sender. name) +  str( ".") +  str( connector. sender. port) +  str( " -> ") +  str( connector. receiver. name) +  str( ".") +  connector. receiver. port        )#line 454

                                                                                #line 455

                                                                                #line 456

def any_child_ready (container):                                                #line 457

    for child in  container. children:                                          #line 458

        if child_is_ready ( child):                                             #line 459

            return  True
                                                                                #line 460


    return  False                                                               #line 461
                                                                                #line 462

                                                                                #line 463

def child_is_ready (eh):                                                        #line 464

    return (not ( eh. outq.empty ())) or (not ( eh. inq.empty ())) or ( eh. state!= "idle") or (any_child_ready ( eh))#line 465
                                                                                #line 466

                                                                                #line 467

def print_routing_trace (eh):                                                   #line 468

    print (routing_trace_all ( eh))                                             #line 469
                                                                                #line 470

                                                                                #line 471

def append_routing_descriptor (container,desc):                                 #line 472

    container. routings.put ( desc)                                             #line 473
                                                                                #line 474

                                                                                #line 475

def container_injector (container,message):                                     #line 476

    container_handler ( container, message)                                     #line 477
                                                                                #line 478

                                                                                #line 479







import os                                                                       #line 1

import json                                                                     #line 2

import sys                                                                      #line 3
                                                                                #line 4
                                                                                #line 5

class Component_Registry:
    def __init__ (self,):                                                       #line 6

        self.templates = {}                                                     #line 7
                                                                                #line 8

                                                                                #line 9

class Template:
    def __init__ (self,name,template_data,instantiator):                        #line 10

        self.name =  name                                                       #line 11

        self.template_data =  template_data                                     #line 12

        self.instantiator =  instantiator                                       #line 13
                                                                                #line 14

                                                                                #line 15

def read_and_convert_json_file (filename):                                      #line 16

    try:
        fil = open(filename, "r")
        json_data = fil.read()
        routings = json.loads(json_data)
        fil.close ()
        return routings
    except FileNotFoundError:
        print (f"File not found: '{filename}'")
        return None
    except json.JSONDecodeError as e:
        print ("Error decoding JSON in file: '{e}'")
        return None
                                                                                #line 17
                                                                                #line 18

                                                                                #line 19

def json2internal (container_xml):                                              #line 20

    fname =  os. path.basename ( container_xml)                                 #line 21

    routings = read_and_convert_json_file ( fname)                              #line 22

    return  routings                                                            #line 23
                                                                                #line 24

                                                                                #line 25

def delete_decls (d):                                                           #line 26

    pass                                                                        #line 27
                                                                                #line 28

                                                                                #line 29

def make_component_registry ():                                                 #line 30

    return Component_Registry ()                                                #line 31
                                                                                #line 32

                                                                                #line 33

def register_component (reg,template):
    return abstracted_register_component ( reg, template, False)                #line 34


def register_component_allow_overwriting (reg,template):
    return abstracted_register_component ( reg, template, True)                 #line 35

                                                                                #line 36

def abstracted_register_component (reg,template,ok_to_overwrite):               #line 37

    name = mangle_name ( template. name)                                        #line 38

    if  name in  reg. templates and not  ok_to_overwrite:                       #line 39

        load_error ( str( "Component ") +  str( template. name) +  " already declared"  )#line 40


    reg. templates [ name] =  template                                          #line 41

    return  reg                                                                 #line 42
                                                                                #line 43

                                                                                #line 44

def register_multiple_components (reg,templates):                               #line 45

    for template in  templates:                                                 #line 46

        register_component ( reg, template)                                     #line 47

                                                                                #line 48

                                                                                #line 49

def get_component_instance (reg,full_name,owner):                               #line 50

    template_name = mangle_name ( full_name)                                    #line 51

    if  template_name in  reg. templates:                                       #line 52

        template =  reg. templates [ template_name]                             #line 53

        if ( template ==  None):                                                #line 54

            load_error ( str( "Registry Error: Can;t find component ") +  str( template_name) +  " (does it need to be declared in components_to_include_in_project?"  )#line 55

            return  None                                                        #line 56

        else:                                                                   #line 57

            owner_name =  ""                                                    #line 58

            instance_name =  template_name                                      #line 59

            if  None!= owner:                                                   #line 60

                owner_name =  owner. name                                       #line 61

                instance_name =  str( owner_name) +  str( ".") +  template_name  #line 62

            else:                                                               #line 63

                instance_name =  template_name                                  #line 64


            instance =  template.instantiator ( reg, owner, instance_name, template. template_data)#line 65

            instance. depth = calculate_depth ( instance)                       #line 66

            return  instance
                                                                                #line 67

    else:                                                                       #line 68

        load_error ( str( "Registry Error: Can't find component ") +  str( template_name) +  " (does it need to be declared in components_to_include_in_project?"  )#line 69

        return  None                                                            #line 70

                                                                                #line 71


def calculate_depth (eh):                                                       #line 72

    if  eh. owner ==  None:                                                     #line 73

        return  0                                                               #line 74

    else:                                                                       #line 75

        return  1+calculate_depth ( eh. owner)                                  #line 76

                                                                                #line 77

                                                                                #line 78

def dump_registry (reg):                                                        #line 79

    print ()                                                                    #line 80

    print ( "*** PALETTE ***")                                                  #line 81

    for c in  reg. templates:                                                   #line 82

        print ( c. name)                                                        #line 83


    print ( "***************")                                                  #line 84

    print ()                                                                    #line 85
                                                                                #line 86

                                                                                #line 87

def print_stats (reg):                                                          #line 88

    print ( str( "registry statistics: ") +  reg. stats )                       #line 89
                                                                                #line 90

                                                                                #line 91

def mangle_name (s):                                                            #line 92

    # trim name to remove code from Container component names _ deferred until later (or never)#line 93

    return  s                                                                   #line 94
                                                                                #line 95

                                                                                #line 96

import subprocess                                                               #line 97

def generate_shell_components (reg,container_list):                             #line 98

    # [                                                                         #line 99

    #     {'file': 'simple0d.drawio', 'name': 'main', 'children': [{'name': 'Echo', 'id': 5}], 'connections': [...]},#line 100

    #     {'file': 'simple0d.drawio', 'name': '...', 'children': [], 'connections': []}#line 101

    # ]                                                                         #line 102

    if  None!= container_list:                                                  #line 103

        for diagram in  container_list:                                         #line 104

            # loop through every component in the diagram and look for names that start with “$“#line 105

            # {'file': 'simple0d.drawio', 'name': 'main', 'children': [{'name': 'Echo', 'id': 5}], 'connections': [...]},#line 106

            for child_descriptor in  diagram ["children"]:                      #line 107

                if first_char_is ( child_descriptor ["name"], "$"):             #line 108

                    name =  child_descriptor ["name"]                           #line 109

                    cmd =   name[1:] .strip ()                                  #line 110

                    generated_leaf = Template ( name, shell_out_instantiate, cmd)#line 111

                    register_component ( reg, generated_leaf)                   #line 112

                elif first_char_is ( child_descriptor ["name"], "'"):           #line 113

                    name =  child_descriptor ["name"]                           #line 114

                    s =   name[1:]                                              #line 115

                    generated_leaf = Template ( name, string_constant_instantiate, s)#line 116

                    register_component_allow_overwriting ( reg, generated_leaf) #line 117
                                                                                #line 118

                                                                                #line 119

                                                                                #line 120

                                                                                #line 121

                                                                                #line 122

                                                                                #line 123

def first_char (s):                                                             #line 124

    return   s[0]                                                               #line 125
                                                                                #line 126

                                                                                #line 127

def first_char_is (s,c):                                                        #line 128

    return  c == first_char ( s)                                                #line 129
                                                                                #line 130

                                                                                #line 131
# this needs to be rewritten to use the low_level “shell_out“ component, this can be done solely as a diagram without using python code here#line 132
# I'll keep it for now, during bootstrapping, since it mimics what is done in the Odin prototype _ both need to be revamped#line 133

def run_command (eh,cmd,s):                                                     #line 134

    # capture_output ∷ ⊤                                                        #line 135

    ret =  subprocess.run ( cmd, s, "UTF_8")                                    #line 136

    if not ( ret. returncode ==  0):                                            #line 137

        if  ret. stderr!= None:                                                 #line 138

            return [ "", ret. stderr]                                           #line 139

        else:                                                                   #line 140

            return [ "", str( "error in shell_out ") +  ret. returncode ]
                                                                                #line 141

    else:                                                                       #line 142

        return [ ret. stdout, None]                                             #line 143

                                                                                #line 144

                                                                                #line 145
# Data for an asyncronous component _ effectively, a function with input        #line 146
# and output queues of messages.                                                #line 147
#                                                                               #line 148
# Components can either be a user_supplied function (“lea“), or a “container“   #line 149
# that routes messages to child components according to a list of connections   #line 150
# that serve as a message routing table.                                        #line 151
#                                                                               #line 152
# Child components themselves can be leaves or other containers.                #line 153
#                                                                               #line 154
# `handler` invokes the code that is attached to this component.                #line 155
#                                                                               #line 156
# `instance_data` is a pointer to instance data that the `leaf_handler`         #line 157
# function may want whenever it is invoked again.                               #line 158
#                                                                               #line 159
                                                                                #line 160

import queue                                                                    #line 161

import sys                                                                      #line 162
                                                                                #line 163
                                                                                #line 164
# Eh_States :: enum { idle, active }                                            #line 165

class Eh:
    def __init__ (self,):                                                       #line 166

        self.name =  ""                                                         #line 167

        self.inq =  queue.Queue ()                                              #line 168

        self.outq =  queue.Queue ()                                             #line 169

        self.owner =  None                                                      #line 170

        self.saved_messages =  queue.LifoQueue () # stack of saved message(s)   #line 171

        self.inject =  injector_NIY                                             #line 172

        self.children = []                                                      #line 173

        self.visit_ordering =  queue.Queue ()                                   #line 174

        self.connections = []                                                   #line 175

        self.routings =  queue.Queue ()                                         #line 176

        self.handler =  None                                                    #line 177

        self.instance_data =  None                                              #line 178

        self.state =  "idle"                                                    #line 179
        # bootstrap debugging                                                   #line 180

        self.kind =  None # enum { container, leaf, }                           #line 181

        self.trace =  False # set '⊤' if logging is enabled and if this component should be traced, (⊥ means silence, no tracing for this component)#line 182

        self.depth =  0 # hierarchical depth of component, 0=top, 1=1st child of top, 2=1st child of 1st child of top, etc.#line 183
                                                                                #line 184

                                                                                #line 185
# Creates a component that acts as a container. It is the same as a `Eh` instance#line 186
# whose handler function is `container_handler`.                                #line 187

def make_container (name,owner):                                                #line 188

    eh = Eh ()                                                                  #line 189

    eh. name =  name                                                            #line 190

    eh. owner =  owner                                                          #line 191

    eh. handler =  container_handler                                            #line 192

    eh. inject =  container_injector                                            #line 193

    eh. state =  "idle"                                                         #line 194

    eh. kind =  "container"                                                     #line 195

    return  eh                                                                  #line 196
                                                                                #line 197

                                                                                #line 198
# Creates a new leaf component out of a handler function, and a data parameter  #line 199
# that will be passed back to your handler when called.                         #line 200
                                                                                #line 201

def make_leaf (name,owner,instance_data,handler):                               #line 202

    eh = Eh ()                                                                  #line 203

    eh. name =  str( owner. name) +  str( ".") +  name                          #line 204

    eh. owner =  owner                                                          #line 205

    eh. handler =  handler                                                      #line 206

    eh. instance_data =  instance_data                                          #line 207

    eh. state =  "idle"                                                         #line 208

    eh. kind =  "leaf"                                                          #line 209

    return  eh                                                                  #line 210
                                                                                #line 211

                                                                                #line 212
# Sends a message on the given `port` with `data`, placing it on the output     #line 213
# of the given component.                                                       #line 214
                                                                                #line 215

def send (eh,port,datum,causingMessage):                                        #line 216

    msg = make_message ( port, datum)                                           #line 217

    put_output ( eh, msg)                                                       #line 218
                                                                                #line 219

                                                                                #line 220

def send_string (eh,port,s,causingMessage):                                     #line 221

    datum = new_datum_string ( s)                                               #line 222

    msg = make_message ( port, datum)                                           #line 223

    put_output ( eh, msg)                                                       #line 224
                                                                                #line 225

                                                                                #line 226

def forward (eh,port,msg):                                                      #line 227

    fwdmsg = make_message ( port, msg. datum)                                   #line 228

    put_output ( eh, msg)                                                       #line 229
                                                                                #line 230

                                                                                #line 231

def inject (eh,msg):                                                            #line 232

    eh.inject ( eh, msg)                                                        #line 233
                                                                                #line 234

                                                                                #line 235
# Returns a list of all output messages on a container.                         #line 236
# For testing / debugging purposes.                                             #line 237
                                                                                #line 238

def output_list (eh):                                                           #line 239

    return  eh. outq                                                            #line 240
                                                                                #line 241

                                                                                #line 242
# Utility for printing an array of messages.                                    #line 243

def print_output_list (eh):                                                     #line 244

    for m in list ( eh. outq. queue):                                           #line 245

        print (format_message ( m))                                             #line 246

                                                                                #line 247

                                                                                #line 248

def spaces (n):                                                                 #line 249

    s =  ""                                                                     #line 250

    for i in range( n):                                                         #line 251

        s =  s+ " "                                                             #line 252


    return  s                                                                   #line 253
                                                                                #line 254

                                                                                #line 255

def set_active (eh):                                                            #line 256

    eh. state =  "active"                                                       #line 257
                                                                                #line 258

                                                                                #line 259

def set_idle (eh):                                                              #line 260

    eh. state =  "idle"                                                         #line 261
                                                                                #line 262

                                                                                #line 263
# Utility for printing a specific output message.                               #line 264
                                                                                #line 265

def fetch_first_output (eh,port):                                               #line 266

    for msg in list ( eh. outq. queue):                                         #line 267

        if ( msg. port ==  port):                                               #line 268

            return  msg. datum
                                                                                #line 269


    return  None                                                                #line 270
                                                                                #line 271

                                                                                #line 272

def print_specific_output (eh,port):                                            #line 273

    # port ∷ “”                                                                 #line 274

    datum = fetch_first_output ( eh, port)                                      #line 275

    outf =  None                                                                #line 276

    if  datum!= None:                                                           #line 277

        outf =  sys. stdout                                                     #line 278

        print ( datum.srepr (), outf)                                           #line 279

                                                                                #line 280


def print_specific_output_to_stderr (eh,port):                                  #line 281

    # port ∷ “”                                                                 #line 282

    datum = fetch_first_output ( eh, port)                                      #line 283

    outf =  None                                                                #line 284

    if  datum!= None:                                                           #line 285

        # I don't remember why I found it useful to print to stderr during bootstrapping, so I've left it in...#line 286

        outf =  sys. stderr                                                     #line 287

        print ( datum.srepr (), outf)                                           #line 288

                                                                                #line 289

                                                                                #line 290

def put_output (eh,msg):                                                        #line 291

    eh. outq.put ( msg)                                                         #line 292
                                                                                #line 293

                                                                                #line 294

def injector_NIY (eh,msg):                                                      #line 295

    # print (f'Injector not implemented for this component “{eh.name}“ kind ∷ {eh.kind} port ∷ “{msg.port}“')#line 296

    print ( str( "Injector not implemented for this component ") +  str( eh. name) +  str( " kind ∷ ") +  str( eh. kind) +  str( ",  port ∷ ") +  msg. port     )#line 301

    exit ()                                                                     #line 302
                                                                                #line 303

                                                                                #line 304

import sys                                                                      #line 305

import re                                                                       #line 306

import subprocess                                                               #line 307

import shlex                                                                    #line 308
                                                                                #line 309

root_project =  ""                                                              #line 310

root_0D =  ""                                                                   #line 311
                                                                                #line 312

def set_environment (rproject,r0D):                                             #line 313

    global root_project                                                         #line 314

    global root_0D                                                              #line 315

    root_project =  rproject                                                    #line 316

    root_0D =  r0D                                                              #line 317
                                                                                #line 318

                                                                                #line 319

def probe_instantiate (reg,owner,name,template_data):                           #line 320

    name_with_id = gensymbol ( "?")                                             #line 321

    return make_leaf ( name_with_id, owner, None, probe_handler)                #line 322
                                                                                #line 323


def probeA_instantiate (reg,owner,name,template_data):                          #line 324

    name_with_id = gensymbol ( "?A")                                            #line 325

    return make_leaf ( name_with_id, owner, None, probe_handler)                #line 326
                                                                                #line 327

                                                                                #line 328

def probeB_instantiate (reg,owner,name,template_data):                          #line 329

    name_with_id = gensymbol ( "?B")                                            #line 330

    return make_leaf ( name_with_id, owner, None, probe_handler)                #line 331
                                                                                #line 332

                                                                                #line 333

def probeC_instantiate (reg,owner,name,template_data):                          #line 334

    name_with_id = gensymbol ( "?C")                                            #line 335

    return make_leaf ( name_with_id, owner, None, probe_handler)                #line 336
                                                                                #line 337

                                                                                #line 338

def probe_handler (eh,msg):                                                     #line 339

    s =  msg. datum.srepr ()                                                    #line 340

    print ( str( "... probe ") +  str( eh. name) +  str( ": ") +  s   , sys. stderr)#line 341
                                                                                #line 342

                                                                                #line 343

def trash_instantiate (reg,owner,name,template_data):                           #line 344

    name_with_id = gensymbol ( "trash")                                         #line 345

    return make_leaf ( name_with_id, owner, None, trash_handler)                #line 346
                                                                                #line 347

                                                                                #line 348

def trash_handler (eh,msg):                                                     #line 349

    # to appease dumped_on_floor checker                                        #line 350

    pass                                                                        #line 351
                                                                                #line 352


class TwoMessages:
    def __init__ (self,first,second):                                           #line 353

        self.first =  first                                                     #line 354

        self.second =  second                                                   #line 355
                                                                                #line 356

                                                                                #line 357
# Deracer_States :: enum { idle, waitingForFirst, waitingForSecond }            #line 358

class Deracer_Instance_Data:
    def __init__ (self,state,buffer):                                           #line 359

        self.state =  state                                                     #line 360

        self.buffer =  buffer                                                   #line 361
                                                                                #line 362

                                                                                #line 363

def reclaim_Buffers_from_heap (inst):                                           #line 364

    pass                                                                        #line 365
                                                                                #line 366

                                                                                #line 367

def deracer_instantiate (reg,owner,name,template_data):                         #line 368

    name_with_id = gensymbol ( "deracer")                                       #line 369

    inst = Deracer_Instance_Data ( "idle",TwoMessages ( None, None))            #line 370

    inst. state =  "idle"                                                       #line 371

    eh = make_leaf ( name_with_id, owner, inst, deracer_handler)                #line 372

    return  eh                                                                  #line 373
                                                                                #line 374

                                                                                #line 375

def send_first_then_second (eh,inst):                                           #line 376

    forward ( eh, "1", inst. buffer. first)                                     #line 377

    forward ( eh, "2", inst. buffer. second)                                    #line 378

    reclaim_Buffers_from_heap ( inst)                                           #line 379
                                                                                #line 380

                                                                                #line 381

def deracer_handler (eh,msg):                                                   #line 382

    inst =  eh. instance_data                                                   #line 383

    if  inst. state ==  "idle":                                                 #line 384

        if  "1" ==  msg. port:                                                  #line 385

            inst. buffer. first =  msg                                          #line 386

            inst. state =  "waitingForSecond"                                   #line 387

        elif  "2" ==  msg. port:                                                #line 388

            inst. buffer. second =  msg                                         #line 389

            inst. state =  "waitingForFirst"                                    #line 390

        else:                                                                   #line 391

            runtime_error ( str( "bad msg.port (case A) for deracer ") +  msg. port )
                                                                                #line 392

    elif  inst. state ==  "waitingForFirst":                                    #line 393

        if  "1" ==  msg. port:                                                  #line 394

            inst. buffer. first =  msg                                          #line 395

            send_first_then_second ( eh, inst)                                  #line 396

            inst. state =  "idle"                                               #line 397

        else:                                                                   #line 398

            runtime_error ( str( "bad msg.port (case B) for deracer ") +  msg. port )
                                                                                #line 399

    elif  inst. state ==  "waitingForSecond":                                   #line 400

        if  "2" ==  msg. port:                                                  #line 401

            inst. buffer. second =  msg                                         #line 402

            send_first_then_second ( eh, inst)                                  #line 403

            inst. state =  "idle"                                               #line 404

        else:                                                                   #line 405

            runtime_error ( str( "bad msg.port (case C) for deracer ") +  msg. port )
                                                                                #line 406

    else:                                                                       #line 407

        runtime_error ( "bad state for deracer {eh.state}")                     #line 408

                                                                                #line 409

                                                                                #line 410

def low_level_read_text_file_instantiate (reg,owner,name,template_data):        #line 411

    name_with_id = gensymbol ( "Low Level Read Text File")                      #line 412

    return make_leaf ( name_with_id, owner, None, low_level_read_text_file_handler)#line 413
                                                                                #line 414

                                                                                #line 415

def low_level_read_text_file_handler (eh,msg):                                  #line 416

    fname =  msg. datum.srepr ()                                                #line 417

    try:
        f = open (fname)
    except Exception as e:
        f = None
    if f != None:
        data = f.read ()
        if data!= None:
            send_string (eh, "", data, msg)
        else:
            send_string (eh, "✗", f"read error on file '{fname}'", msg)
        f.close ()
    else:
        send_string (eh, "✗", f"open error on file '{fname}'", msg)
                                                                                #line 418
                                                                                #line 419

                                                                                #line 420

def ensure_string_datum_instantiate (reg,owner,name,template_data):             #line 421

    name_with_id = gensymbol ( "Ensure String Datum")                           #line 422

    return make_leaf ( name_with_id, owner, None, ensure_string_datum_handler)  #line 423
                                                                                #line 424

                                                                                #line 425

def ensure_string_datum_handler (eh,msg):                                       #line 426

    if  "string" ==  msg. datum.kind ():                                        #line 427

        forward ( eh, "", msg)                                                  #line 428

    else:                                                                       #line 429

        emsg =  str( "*** ensure: type error (expected a string datum) but got ") +  msg. datum #line 430

        send_string ( eh, "✗", emsg, msg)                                       #line 431

                                                                                #line 432

                                                                                #line 433

class Syncfilewrite_Data:
    def __init__ (self,):                                                       #line 434

        self.filename =  ""                                                     #line 435
                                                                                #line 436

                                                                                #line 437
# temp copy for bootstrap, sends “done“ (error during bootstrap if not wired)   #line 438

def syncfilewrite_instantiate (reg,owner,name,template_data):                   #line 439

    name_with_id = gensymbol ( "syncfilewrite")                                 #line 440

    inst = Syncfilewrite_Data ()                                                #line 441

    return make_leaf ( name_with_id, owner, inst, syncfilewrite_handler)        #line 442
                                                                                #line 443

                                                                                #line 444

def syncfilewrite_handler (eh,msg):                                             #line 445

    inst =  eh. instance_data                                                   #line 446

    if  "filename" ==  msg. port:                                               #line 447

        inst. filename =  msg. datum.srepr ()                                   #line 448

    elif  "input" ==  msg. port:                                                #line 449

        contents =  msg. datum.srepr ()                                         #line 450

        f = open ( inst. filename, "w")                                         #line 451

        if  f!= None:                                                           #line 452

            f.write ( msg. datum.srepr ())                                      #line 453

            f.close ()                                                          #line 454

            send ( eh, "done",new_datum_bang (), msg)                           #line 455

        else:                                                                   #line 456

            send_string ( eh, "✗", str( "open error on file ") +  inst. filename , msg)
                                                                                #line 457

                                                                                #line 458

                                                                                #line 459

class StringConcat_Instance_Data:
    def __init__ (self,):                                                       #line 460

        self.buffer1 =  None                                                    #line 461

        self.buffer2 =  None                                                    #line 462

        self.count =  0                                                         #line 463
                                                                                #line 464

                                                                                #line 465

def stringconcat_instantiate (reg,owner,name,template_data):                    #line 466

    name_with_id = gensymbol ( "stringconcat")                                  #line 467

    instp = StringConcat_Instance_Data ()                                       #line 468

    return make_leaf ( name_with_id, owner, instp, stringconcat_handler)        #line 469
                                                                                #line 470

                                                                                #line 471

def stringconcat_handler (eh,msg):                                              #line 472

    inst =  eh. instance_data                                                   #line 473

    if  "1" ==  msg. port:                                                      #line 474

        inst. buffer1 = clone_string ( msg. datum.srepr ())                     #line 475

        inst. count =  inst. count+ 1                                           #line 476

        maybe_stringconcat ( eh, inst, msg)                                     #line 477

    elif  "2" ==  msg. port:                                                    #line 478

        inst. buffer2 = clone_string ( msg. datum.srepr ())                     #line 479

        inst. count =  inst. count+ 1                                           #line 480

        maybe_stringconcat ( eh, inst, msg)                                     #line 481

    else:                                                                       #line 482

        runtime_error ( str( "bad msg.port for stringconcat: ") +  msg. port )  #line 483
                                                                                #line 484

                                                                                #line 485

                                                                                #line 486

def maybe_stringconcat (eh,inst,msg):                                           #line 487

    if ( 0 == len ( inst. buffer1)) and ( 0 == len ( inst. buffer2)):           #line 488

        runtime_error ( "something is wrong in stringconcat, both strings are 0 length")#line 489


    if  inst. count >=  2:                                                      #line 490

        concatenated_string =  ""                                               #line 491

        if  0 == len ( inst. buffer1):                                          #line 492

            concatenated_string =  inst. buffer2                                #line 493

        elif  0 == len ( inst. buffer2):                                        #line 494

            concatenated_string =  inst. buffer1                                #line 495

        else:                                                                   #line 496

            concatenated_string =  inst. buffer1+ inst. buffer2                 #line 497


        send_string ( eh, "", concatenated_string, msg)                         #line 498

        inst. buffer1 =  None                                                   #line 499

        inst. buffer2 =  None                                                   #line 500

        inst. count =  0                                                        #line 501

                                                                                #line 502

                                                                                #line 503
#                                                                               #line 504
                                                                                #line 505
# this needs to be rewritten to use the low_level “shell_out“ component, this can be done solely as a diagram without using python code here#line 506

def shell_out_instantiate (reg,owner,name,template_data):                       #line 507

    name_with_id = gensymbol ( "shell_out")                                     #line 508

    cmd =  shlex.split ( template_data)                                         #line 509

    return make_leaf ( name_with_id, owner, cmd, shell_out_handler)             #line 510
                                                                                #line 511

                                                                                #line 512

def shell_out_handler (eh,msg):                                                 #line 513

    cmd =  eh. instance_data                                                    #line 514

    s =  msg. datum.srepr ()                                                    #line 515

    [ stdout, stderr] = run_command ( eh, cmd, s)                               #line 516

    if  stderr!= None:                                                          #line 517

        send_string ( eh, "✗", stderr, msg)                                     #line 518

    else:                                                                       #line 519

        send_string ( eh, "", stdout, msg)                                      #line 520

                                                                                #line 521

                                                                                #line 522

def string_constant_instantiate (reg,owner,name,template_data):                 #line 523

    global root_project                                                         #line 524

    global root_0D                                                              #line 525

    name_with_id = gensymbol ( "strconst")                                      #line 526

    s =  template_data                                                          #line 527

    if  root_project!= "":                                                      #line 528

        s =  re.sub ( "_00_", root_project, s)                                  #line 529


    if  root_0D!= "":                                                           #line 530

        s =  re.sub ( "_0D_", root_0D, s)                                       #line 531


    return make_leaf ( name_with_id, owner, s, string_constant_handler)         #line 532
                                                                                #line 533

                                                                                #line 534

def string_constant_handler (eh,msg):                                           #line 535

    s =  eh. instance_data                                                      #line 536

    send_string ( eh, "", s, msg)                                               #line 537
                                                                                #line 538

                                                                                #line 539

def string_make_persistent (s):                                                 #line 540

    # this is here for non_GC languages like Odin, it is a no_op for GC languages like Python#line 541

    return  s                                                                   #line 542
                                                                                #line 543

                                                                                #line 544

def string_clone (s):                                                           #line 545

    return  s                                                                   #line 546
                                                                                #line 547

                                                                                #line 548

import sys                                                                      #line 549
                                                                                #line 550
# usage: app ${_00_} ${_0D_} arg main diagram_filename1 diagram_filename2 ...   #line 551
# where ${_00_} is the root directory for the project                           #line 552
# where ${_0D_} is the root directory for 0D (e.g. 0D/odin or 0D/python)        #line 553
                                                                                #line 554
                                                                                #line 555
                                                                                #line 556

def initialize_component_palette (root_project,root_0D,diagram_source_files):   #line 557

    reg = make_component_registry ()                                            #line 558

    for diagram_source in  diagram_source_files:                                #line 559

        all_containers_within_single_file = json2internal ( diagram_source)     #line 560

        generate_shell_components ( reg, all_containers_within_single_file)     #line 561

        for container in  all_containers_within_single_file:                    #line 562

            register_component ( reg,Template ( container ["name"], container, container_instantiator))
                                                                                #line 563


    initialize_stock_components ( reg)                                          #line 564

    return  reg                                                                 #line 565
                                                                                #line 566

                                                                                #line 567

def print_error_maybe (main_container):                                         #line 568

    error_port =  "✗"                                                           #line 569

    err = fetch_first_output ( main_container, error_port)                      #line 570

    if ( err!= None) and ( 0 < len (trimws ( err.srepr ()))):                   #line 571

        print ( "___ !!! ERRORS !!! ___")                                       #line 572

        print_specific_output ( main_container, error_port, False)              #line 573

                                                                                #line 574

                                                                                #line 575
# debugging helpers                                                             #line 576
                                                                                #line 577

def dump_outputs (main_container):                                              #line 578

    print ()                                                                    #line 579

    print ( "___ Outputs ___")                                                  #line 580

    print_output_list ( main_container)                                         #line 581
                                                                                #line 582

                                                                                #line 583

def trace_outputs (main_container):                                             #line 584

    print ()                                                                    #line 585

    print ( "___ Message Traces ___")                                           #line 586

    print_routing_trace ( main_container)                                       #line 587
                                                                                #line 588

                                                                                #line 589

def dump_hierarchy (main_container):                                            #line 590

    print ()                                                                    #line 591

    print ( str( "___ Hierarchy ___") + (build_hierarchy ( main_container)) )   #line 592
                                                                                #line 593

                                                                                #line 594

def build_hierarchy (c):                                                        #line 595

    s =  ""                                                                     #line 596

    for child in  c. children:                                                  #line 597

        s =  str( s) + build_hierarchy ( child)                                 #line 598


    indent =  ""                                                                #line 599

    for i in range( c. depth):                                                  #line 600

        indent =  indent+ "  "                                                  #line 601


    return  str( "\n") +  str( indent) +  str( "(") +  str( c. name) +  str( s) +  ")"     #line 602
                                                                                #line 603

                                                                                #line 604

def dump_connections (c):                                                       #line 605

    print ()                                                                    #line 606

    print ( "___ connections ___")                                              #line 607

    dump_possible_connections ( c)                                              #line 608

    for child in  c. children:                                                  #line 609

        print ()                                                                #line 610

        dump_possible_connections ( child)                                      #line 611

                                                                                #line 612

                                                                                #line 613

def trimws (s):                                                                 #line 614

    # remove whitespace from front and back of string                           #line 615

    return  s.strip ()                                                          #line 616
                                                                                #line 617

                                                                                #line 618

def clone_string (s):                                                           #line 619

    return  s                                                                   #line 620
                                                                                #line 621
                                                                                #line 622


load_errors =  False                                                            #line 623

runtime_errors =  False                                                         #line 624
                                                                                #line 625

def load_error (s):                                                             #line 626

    global load_errors                                                          #line 627

    print ( s)                                                                  #line 628

    quit ()                                                                     #line 629

    load_errors =  True                                                         #line 630
                                                                                #line 631

                                                                                #line 632

def runtime_error (s):                                                          #line 633

    global runtime_errors                                                       #line 634

    print ( s)                                                                  #line 635

    quit ()                                                                     #line 636

    runtime_errors =  True                                                      #line 637
                                                                                #line 638

                                                                                #line 639

def fakepipename_instantiate (reg,owner,name,template_data):                    #line 640

    instance_name = gensymbol ( "fakepipe")                                     #line 641

    return make_leaf ( instance_name, owner, None, fakepipename_handler)        #line 642
                                                                                #line 643

                                                                                #line 644

rand =  0                                                                       #line 645
                                                                                #line 646

def fakepipename_handler (eh,msg):                                              #line 647

    global rand                                                                 #line 648

    rand =  rand+ 1
    # not very random, but good enough _ 'rand' must be unique within a single run#line 649

    send_string ( eh, "", str( "/tmp/fakepipe") +  rand , msg)                  #line 650
                                                                                #line 651

                                                                                #line 652
                                                                                #line 653
# all of the the built_in leaves are listed here                                #line 654
# future: refactor this such that programmers can pick and choose which (lumps of) builtins are used in a specific project#line 655
                                                                                #line 656
                                                                                #line 657

def initialize_stock_components (reg):                                          #line 658

    register_component ( reg,Template ( "1then2", None, deracer_instantiate))   #line 659

    register_component ( reg,Template ( "?", None, probe_instantiate))          #line 660

    register_component ( reg,Template ( "?A", None, probeA_instantiate))        #line 661

    register_component ( reg,Template ( "?B", None, probeB_instantiate))        #line 662

    register_component ( reg,Template ( "?C", None, probeC_instantiate))        #line 663

    register_component ( reg,Template ( "trash", None, trash_instantiate))      #line 664
                                                                                #line 665

    register_component ( reg,Template ( "Low Level Read Text File", None, low_level_read_text_file_instantiate))#line 666

    register_component ( reg,Template ( "Ensure String Datum", None, ensure_string_datum_instantiate))#line 667
                                                                                #line 668

    register_component ( reg,Template ( "syncfilewrite", None, syncfilewrite_instantiate))#line 669

    register_component ( reg,Template ( "stringconcat", None, stringconcat_instantiate))#line 670

    # for fakepipe                                                              #line 671

    register_component ( reg,Template ( "fakepipename", None, fakepipename_instantiate))#line 672
                                                                                #line 673

                                                                                #line 674
                                                                                #line 675

def initialize ():                                                              #line 676

    root_of_project =  sys.argv[ 1]                                             #line 677

    root_of_0D =  sys.argv[ 2]                                                  #line 678

    arg =  sys.argv[ 3]                                                         #line 679

    main_container_name =  sys.argv[ 4]                                         #line 680

    diagram_names =  sys.argv[ 5:]                                              #line 681

    palette = initialize_component_palette ( root_project, root_0D, diagram_names)#line 682

    return [ palette,[ root_of_project, root_of_0D, main_container_name, diagram_names, arg]]#line 683
                                                                                #line 684

                                                                                #line 685

def start (palette,env):
    start_with_debug ( palette, env, False, False, False, False)                #line 686


def start_with_debug (palette,env,show_hierarchy,show_connections,show_traces,show_all_outputs):#line 687

    # show_hierarchy∷⊥, show_connections∷⊥, show_traces∷⊥, show_all_outputs∷⊥   #line 688

    root_of_project =  env [ 0]                                                 #line 689

    root_of_0D =  env [ 1]                                                      #line 690

    main_container_name =  env [ 2]                                             #line 691

    diagram_names =  env [ 3]                                                   #line 692

    arg =  env [ 4]                                                             #line 693

    set_environment ( root_of_project, root_of_0D)                              #line 694

    # get entrypoint container                                                  #line 695

    main_container = get_component_instance ( palette, main_container_name, None)#line 696

    if  None ==  main_container:                                                #line 697

        load_error ( str( "Couldn't find container with page name ") +  str( main_container_name) +  str( " in files ") +  str( diagram_names) +  "(check tab names, or disable compression?)"    )#line 701
                                                                                #line 702


    if  show_hierarchy:                                                         #line 703

        dump_hierarchy ( main_container)                                        #line 704
                                                                                #line 705


    if  show_connections:                                                       #line 706

        dump_connections ( main_container)                                      #line 707
                                                                                #line 708


    if not  load_errors:                                                        #line 709

        arg = new_datum_string ( arg)                                           #line 710

        msg = make_message ( "", arg)                                           #line 711

        inject ( main_container, msg)                                           #line 712

        if  show_all_outputs:                                                   #line 713

            dump_outputs ( main_container)                                      #line 714

        else:                                                                   #line 715

            print_error_maybe ( main_container)                                 #line 716

            print_specific_output ( main_container, "")                         #line 717

            if  show_traces:                                                    #line 718

                print ( "--- routing traces ---")                               #line 719

                print (routing_trace_all ( main_container))                     #line 720
                                                                                #line 721

                                                                                #line 722


        if  show_all_outputs:                                                   #line 723

            print ( "--- done ---")                                             #line 724
                                                                                #line 725

                                                                                #line 726

                                                                                #line 727

                                                                                #line 728
                                                                                #line 729
                                                                                #line 730
# utility functions                                                             #line 731

def send_int (eh,port,i,causing_message):                                       #line 732

    datum = new_datum_int ( i)                                                  #line 733

    send ( eh, port, datum, causing_message)                                    #line 734
                                                                                #line 735

                                                                                #line 736

def send_bang (eh,port,causing_message):                                        #line 737

    datum = new_datum_bang ()                                                   #line 738

    send ( eh, port, datum, causing_message)                                    #line 739
                                                                                #line 740

                                                                                #line 741





