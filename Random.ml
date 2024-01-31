open Random

let rec read_int_safe () =
  try Some (read_int ()) with
  | End_of_file -> None
  | Failure _ -> None

let () =
  Random.self_init ();
  let target = Random.int 100 in
  let rec guess_number () =
    print_endline "Guess the number between 0 and 99:";
    match read_int_safe () with
    | Some x when x < target -> print_endline "Too low!"; guess_number ()
    | Some x when x > target -> print_endline "Too high!"; guess_number ()
    | Some _ -> print_endline "Congratulations, you guessed it!"
    | None -> print_endline "Error: Input ended unexpectedly."
  in
  
  guess_number ()
